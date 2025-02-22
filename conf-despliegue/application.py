from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    '''Index page route'''
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    '''Procesa el formulario y muestra la página hello.html'''
    name = request.form.get('name', 'Anónimo')
    return render_template('hello.html', name=name)