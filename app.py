from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')