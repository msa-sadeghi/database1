from base_model import BaseModel

class User(BaseModel):
    table_name = "users"

    def create(self, data):
        query = """
            INSERT INTO users
            (username, password_hash, full_name, role, is_active)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """
        params = (
            data['username'], data['password_hash'], data.get('full_name'),
            data.get('role', 'operator'), data.get('is_active', True)
        )
        return self.db.execute_query(query, params)

    def update(self, id, data):
        query = """
            UPDATE users SET
                full_name = %s,
                role = %s,
                is_active = %s
            WHERE id = %s
        """
        params = (data['full_name'], data['role'], data['is_active'], id)
        return self.db.execute_query(query, params)
    
    def get_by_username(self, username):
        query = "SELECT * FROM users WHERE username = %s LIMIT 1"
        params = (username,)
        return self.db.fetch_one(query, params)
