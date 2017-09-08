from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsMyKey" # required to use session

@app.route('/', methods=['POST', 'GET'])
def index():
      if (request.method == 'GET'):
            print request.method
            session['countkey'] += 1
      elif (request.method =="POST"):
          if request.form['action'] == 'reset':
              session['countkey'] = 0
          elif request.form['action'] == 'add2':
              session['countkey'] += 2
            

      return render_template("index.html", sessionVal=session['countkey'])


app.run(debug=True) # run our servera