from flask import Flask 

app = Flask(__name__) 
# always have an instance for flask

@app.route('/')
def index():
    return "Hello" 
# can return what you want in server

if __name__=="__main__": 
    app.run(debug=True)
# debug is for developing only 


