from flask_app.config.mysqlconnection import connect

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Dojo_id = ['Dojo_id'] 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.Dojo_id;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connect('dojos_and_ninjas_schema').run_query(query)
    # Create an empty list to append our instances of friends
        ninjas = []
    # Iterate over the db results and create instances of friends with cls.
        if results:
            for row in results:
                new_ninja = cls(row) 
                ninjas.append(new_ninja)
            return ninjas
        

    @classmethod 
    def new(cls,data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, Dojo_id) 
        VALUES(%(first_name)s,%(last_name)s,%(age)s,%(Dojo_id)s)
        """
        result = connect('dojos_and_ninjas_schema').run_query(query,data) 
        return result 
    
    @classmethod 
    def save(cls,data):
        query = "SELECT * FROM ninjas WHERE name = %(name)s;"
        result = connect('dojos_and_ninjas_schema').run_query(query,data)
        return result
