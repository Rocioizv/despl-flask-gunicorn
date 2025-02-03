
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    '''Index page route'''
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    '''hello.html page route'''
    name = request.form.get('name')
    return render_template('hello.html', name=name)
