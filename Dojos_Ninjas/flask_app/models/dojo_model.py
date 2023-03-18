# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connect 
from flask_app.models import ninja_model
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connect('dojos_and_ninjas_schema').run_query(query)
    # Create an empty list to append our instances of friends
        dojos = []
    # Iterate over the db results and create instances of friends with cls.
        if results:
            for row in results:
                new_dojo = cls(row) 
                dojos.append(new_dojo)
            return dojos
        

    @classmethod 
    def create(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        result = connect('dojos_and_ninjas_schema').run_query(query,data)
        return result

    @classmethod 
    def save(cls,data):
        query = "SELECT * FROM dojos WHERE name = %(name)s;"
        result = connect('dojos_and_ninjas_schema').run_query(query,data)
        return result
    
    @classmethod 
    def show(cls,id):
        
        data = {
        "id": id
        }
        
        query = """
        SELECT * FROM dojos 
        JOIN ninjas ON ninjas.Dojo_id = dojos.id WHERE dojos.id = %(id)s;
        """

        results = connect('dojos_and_ninjas_schema').run_query(query,data)
        
        if results: 
            dojo = cls(results[0]) 

            ninjas = []
            for row in results:
                ninjas_data = {
                    **row, 
                    'id' : row['ninjas.id'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at']
                }

                new_ninja = ninja_model.Ninja(ninjas_data)

                ninjas.append(new_ninja)
            
            dojo.ninjas = ninjas

        return dojo
