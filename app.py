import webbrowser
from flask import Flask, render_template,request,redirect,session, flash, jsonify,url_for
from flask_bootstrap import Bootstrap

app = Flask('ASLLearn')

Bootstrap(app)
app.config['SECRET_KEY'] = "mypandaisgone"


@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug = True, port= '5000')