from flask import Flask, render_template
app = Flask(__name__)
#decorater to multiplate the work 
#app can be change with any name eg:project
@app. route('/')
def home():
    return render_template('cute.html')


@app.route('/about')
def about():
    return"about Kawa Designs"

