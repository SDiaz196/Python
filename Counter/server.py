from flask import Flask, render_template, redirect, session

app = Flask(__name__) 
app.secret_key = "session"

@app.route('/') 
def index(): 
    if "num" not in session: 
        session["num"] = 1
    else:
        session["num"] += 1
    return render_template("index.html") 

@app.route('/count') 
def count():
    session["num"] += 1
    return redirect('/') 

@app.route('/destroy_session') 
def destroy(): 
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)