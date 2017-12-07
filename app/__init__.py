from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/pertama')
def pertama():
    a = 1
    return render_template('index.html', data=a)

@app.route('/kedua')
def kedua():
    a = ['restu', 'restu2', 'restu2']
    return render_template('halaman2.html', data=a)

@app.route('/login', methods=['POST','GET'])
def login():
    username = 'test'
    password = 'test123'

    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

    return render_template('login.html')