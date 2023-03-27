from flask import Flask,render_template,session,request,redirect 
# importing everything we will be using in this server

app = Flask(__name__) 
# instance for flask 
app.secret_key = "session" 
# security for session 

@app.route('/')
def index(): 
    session.clear()
    return render_template('index.html')  



@app.route('/result',methods=["POST"])
def result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/display')


@app.route('/display')
def display():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True) 
# debugger code 
