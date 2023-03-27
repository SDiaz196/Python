from flask import Flask 

app = Flask(__name__) 
# always have an instance for flask

@app.route('/')
def index():
    return "Hello World!" 
# can return what you want in server

@app.route('/dojo')
def dojo():
    return "Dojo!" 

@app.route('/say/<name>') 
def say(name): 
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num,name):
    return f"{name * num}" 

@app.route('/<error>')
def error(error): 
    return "Sorry! No response. Try again."

if __name__=="__main__": 
    app.run(debug=True)
# debug is for developing only 