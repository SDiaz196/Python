from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo_model import Dojo 
from flask_app.models.ninja_model import Ninja 



@app.route('/ninjas')
def ninja():
    return render_template('ninja.html', dojos = Dojo.get_all()) 

@app.route('/ninjas/new',methods=['POST'])
def new():
    Ninja.new(request.form)
    return redirect('/dojos')