from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user_model import User

@app.route('/users')
def index():
    user = User.get_all()
    return render_template('index.html',users = user)

@app.route('/users/new')
def new():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create():
    User.create(request.form)
    print(request.form) 
    return redirect('/users')

@app.route('/users/save/<int:id>', methods=['POST'])
def save(id):
    User.edit(request.form,id)
    return redirect('/users') 

@app.route('/users/show/<int:id>')
def show(id):
    user = User.get_one(id)
    return render_template('show.html',user = user)


@app.route('/users/update/<int:id>') 
def update(id):
    user = User.get_one(id)
    return render_template('update.html',user = user)

@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/users')