# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connect
from flask_app import bcrypt, DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id'] 
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def create(cls,form):
        hashed_pw = bcrypt.generate_password_hash(form['password'])
        data = { 
            **form, 
            'password' : hashed_pw 
        }

        query = """
        INSERT INTO user(first_name,last_name,email,password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """
        return connect(DATABASE).run_query(query,data)
    
    @classmethod 
    def get_one(cls,email):
        data = {
            'email': email,
        }
        query = "SELECT * FROM user WHERE email = %(email)s"
        
        results = connect(DATABASE).run_query(query,data)

        if results:
            user = cls(results[0])
            return user
        else:
            return False 
        
    @classmethod 
    def get_one_name(cls,id):
        data = {
            'id': id,
        }
        query = "SELECT * FROM user WHERE id = %(id)s"
        
        results = connect(DATABASE).run_query(query,data)

        if results:
            user = cls(results[0])
            return user
        else:
            return False 
        

    @classmethod 
    def validate(cls,form):
        is_valid = True 

        if len(form['first_name']) < 2:
            is_valid = False 
            flash('First name must be at least 2 characters!')
        if len(form['last_name']) < 2:
            is_valid = False 
            flash('Last name must be at least 2 characters!')
        if not EMAIL_REGEX.match(form['email']):
            is_valid = False 
            flash('Invalid email')
        if len(form['password']) < 8: 
            is_valid = False 
            flash("Password must be at least 8 characters!")
        if form['password'] != form ['confirm_password']:
            is_valid = False 
            flash('Passwords do not match')

        return is_valid

    @classmethod 
    def validate_login(cls,form): 
        found_user = cls.get_one(form['email'])

        if found_user:
            if bcrypt.check_password_hash(found_user.password,form['password']):
                return found_user 
            else:
                flash('Invalid login!')
                return False 
        else:
            flash('Invalid login!')
            return False 
