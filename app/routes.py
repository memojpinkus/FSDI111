from flask import Flask                     #from the flask module import the Flask class
from datetime import datetime               

app = Flask(__name__)                       #create an instance of "Flask" into app
                                            #the "app" variable is also considered an "object"

@app.get("/")                               #Flask decorator that allows us to map "/" to "index"
def index():                                #Python function - in Flask this is a "view function"
    me = {                                  #Python dictionary containing key-value pairs
        "first_name": "Memo",
        "last_name": "Pinkus",
        "hobbies": "Playing guitar",
        "active": True
    }
    return me                               #return statement, Flask converts dict to JSON