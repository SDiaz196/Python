# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connect
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connect('users_schema').run_query(query)
    # Create an empty list to append our instances of friends
        users = []
    # Iterate over the db results and create instances of friends with cls.
        if results:
            for row in results:
                new_user = cls(row) 
                users.append(new_user)
            return users

    @classmethod 
    def create(cls,data):
        query = """
        INSERT INTO users (first_name,last_name,email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        return connect('users_schema').run_query(query,data)

    def __repr__(self):
        return self.first_name

    @classmethod 
    def get_one(cls,id):
        query = "SELECT * FROM users WHERE id= %(id)s"
        data = {
            'id':id
        }
        result = connect('users_schema').run_query(query,data)
        return cls(result[0])

    @classmethod 
    def delete(cls, id):
        data = {
            'id':id
        } 
        query = "DELETE FROM users WHERE id = %(id)s"
        return connect('users_schema').run_query(query,data) 
    
    @classmethod 
    def edit(cls,form,id):
        data = {
            **form,
            'id':id
        }
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        return connect('users_schema').run_query(query,data)

