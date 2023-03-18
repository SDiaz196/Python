from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo_model import Dojo 
from flask_app.models.ninja_model import Ninja

@app.route('/dojos') 
def dojo():
    return render_template('index.html', dojos = Dojo.get_all()) 

@app.route('/create', methods=['POST'])
def create():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/show/<int:id>') 
def show(id):
    return render_template('show.html', dojos = Dojo.show(id))