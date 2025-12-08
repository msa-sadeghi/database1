from base_model import BaseModel

class Installment(BaseModel):
    table_name = "installments"

    def create(self, data):
        query = """
            INSERT INTO installments
            (loan_id, installment_number, due_date, amount,
             paid_amount, status, paid_date, delays_days)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        params = (
            data['loan_id'], data['installment_number'], data['due_date'],
            data['amount'], data.get('paid_amount', 0),
            data.get('status', 'pending'), data.get('paid_date'),
            data.get('delays_days', 0)
        )
        return self.db.execute_query(query, params)

    def pay(self, installment_id, amount, paid_date):
        query = """
            UPDATE installments
            SET paid_amount = paid_amount + %s,
                paid_date = %s,
                status = 'paid'
            WHERE id = %s
        """
        params = (amount, paid_date, installment_id)
        return self.db.execute_query(query, params)
