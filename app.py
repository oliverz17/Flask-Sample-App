#from __future__ import print_function
from flask import Flask, redirect, url_for
from flask import request
from flask import render_template
from werkzeug import secure_filename

#put functions here


app = Flask(__name__, static_url_path='') #create the Flask app

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def first_visit():
    return redirect(url_for('show_home'))

@app.route('/home', methods=['GET', 'POST']) #allow both GET and POST requests
def show_home():
    return render_template('Home.html')

@app.route('/about', methods=['GET', 'POST']) #allow both GET and POST requests
def show_about():
    return render_template ('About.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080) 
