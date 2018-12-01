from flask import Flask, render_template
app = Flask(__name__)

fruits =['banana','orange','grapes','mangoes','jackfruit','apple']
@app.route('/')
def home():
    return render_template('fruits.html',fruits=fruits)

@app.route('/about')
def about():
    return"about My Fruits"

animals =['cow','pig','goat','loin','dear']

@app.route('/animals')

def man():

    return render_template('animals.html',animals=animals)

@app.route('/sink') 

def sink():
    
    return"about My animals"

