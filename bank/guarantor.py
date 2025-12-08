from base_model import BaseModel

class Guarantor(BaseModel):
    table_name = "guarantors"

    def create(self, data):
        query = """
            INSERT INTO guarantors
            (loan_id, national_code, first_name, last_name, phone, address, relationship)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        params = (
            data['loan_id'], data['national_code'], data['first_name'],
            data['last_name'], data.get('phone'),
            data.get('address'), data.get('relationship')
        )
        return self.db.execute_query(query, params)

    def update(self, id, data):
        query = """
            UPDATE guarantors SET
            phone = %s, address = %s, relationship = %s
            WHERE id = %s
        """
        params = (data['phone'], data['address'], data['relationship'], id)
        return self.db.execute_query(query, params)
