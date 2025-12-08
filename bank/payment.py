from base_model import BaseModel

class Payment(BaseModel):
    table_name = "payments"

    def create(self, data):
        query = """
            INSERT INTO payments
            (installment_id, amount, payment_date,
             payment_method, reference_number, description)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        params = (
            data['installment_id'], data['amount'], data['payment_date'],
            data.get('payment_method'), data.get('reference_number'),
            data.get('description')
        )
        return self.db.execute_query(query, params)

    def update(self, id, data):
        query = """
            UPDATE payments SET
                amount = %s,
                payment_date = %s,
                payment_method = %s,
                reference_number = %s,
                description = %s
            WHERE id = %s
        """
        params = (
            data['amount'], data['payment_date'], data['payment_method'],
            data['reference_number'], data['description'], id
        )
        return self.db.execute_query(query, params)
