from flask import Flask, render_template
app = Flask(__name__)
posts=[
    {"title":"My first post",
    "content":"content for my frist post",
    "author":"Angel",
    "date":"19.11.2018",
    "year":"2018"

    },
    {"title":"My first post",
    "content":"content for my second post",
    "author":"Dear",
    "date":"18.11.2017",
    "year":"2017"

    },
    {
         "title":"My first post",
     "content":"content for my third post",
    "author":"Joan",
     "date":"17.11.2016",
     "year":"2016"



    },
    {
         "title":"My first post",
   "content":"content for my forth post",
     "author":"Noeline",
     "date":"16.11.2015",
     "year":"2015"

     },
     {
         "title":"My first post",
   "content":"content for my forth post",
     "author":"Victor",
     "date":"16.11.2014",
    "year":"2014"




     },
    
]

@app.route('/')
def home():
    return render_template('hi.html',posts=posts)


@app.route('/about')
def about():
    return"about Kampabits"

