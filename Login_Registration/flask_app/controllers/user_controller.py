from flask_app import app
from flask import render_template,redirect,request,session 
from flask_app.models.user_model import User


@app.route('/')          
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    User.create(request.form)
    return redirect('/welcome')

@app.route('/login', methods=['POST'])
def login():
    log_in_user = User.validate_login(request.form)
    if log_in_user:
        session['id'] = log_in_user.id
        return redirect('/welcome')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/welcome')
def welcome():
    if "id" not in session:
        return redirect('/')
    user = User.get_one_name(session['id'])
    return render_template('welcome.html', user=user)