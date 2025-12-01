from base_model import BaseModel
from datetime import datetime, timedelta

class Loan(BaseModel):
    table_name = "loans"
    def create(self, data):
        query ="""
                INSERT INTO loans
                (borrower_id, loan_amount, installment_count, installment_amount,
                start_date, loan_type, description
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """
        params = (
            data['borrower_id'], data['loan_amount'], data['installment_count'], 
            data['installment_amount'],  data['start_date'], data['loan_type'], data['description']
        )
        result = self.db.execute_query(query, params)
        self._create_installment(result, data)
        return result
    
    def _create_installment(self, loan_id, loan_data):
        start_date = datetime.strptime(loan_data['start_date'],  '%Y-%m-%d')
        installment_amount = loan_data['installment_amount']
        installment_count = loan_data['installment_count']

        for i in range(1, installment_count +  1):
            due_date = start_date + timedelta(days=30 * i)
            query = """
                INSERT INTO installments (loan_id, installment_number, due_date, amount)
                VALUES (%s,  %s, %s, %s)
                    """
            self.db.execute_query(query, (loan_id, i,  due_date, installment_amount))

    
    
    