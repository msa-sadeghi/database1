from base_model import BaseModel


class Borrower(BaseModel):
    table_name = "borrowers"
    def create(self, data):
        query ="""
                INSERT INTO borrowers
                (national_code, first_name, last_name, father_name,
                birth_date, phone, mobile, address, postal_code
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """
        params = (
            data['national_code'], data['first_name'], data['last_name'], 
            data['father_name'],  data['birth_date'], data['phone'], data['mobile'], 
            data['address'],  data['postal_code']
        )
        return self.db.execute_query(query, params)
    def update(self, id, data):
        query = """
            UPDATE borrowers SET 
            first_name = %s, last_name = %s, phone = %s,
            mobile = %s, address = %s
            WHERE id = %s    
        """
        params = (
            data['first_name'], data['last_name'], data['phone'], data['mobile'], data['address'], id
        )
        return self.db.execute_query(query, params)
    def search(self, keyword):
        query = """
            SELECT * FROM borrowers
            WHERE national_code LIKE %s
            OR first_name LIKE %s
            OR last_name LIKE %s
            OR phone LIKE %s   
        """
        
        return self.db.execute_query(query, (keyword,))
    


b  = Borrower()
data= {
}
data['national_code'] = "12345677" 
data['first_name'] = "alireza" 
data['last_name'] = "rezaei" 
data['father_name'] = "javad"
data['birth_date'] = "2020-01-01"
data['phone'] = "123333"
data['mobile'] = "222222" 
data['address'] = "teh"  
data['postal_code'] = "000000000"
b.create(data)