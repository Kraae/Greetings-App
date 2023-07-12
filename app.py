
"""Flask Greet"""

"""
Make a simple flask app that responds
to these routes with simple text messages"

/welcome = Returns "welcome"

/welcome/home = Returns "welcome home"

/welcome/back = Returns "welcome back"
"""

from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
        return "Welcome!"

@app.route('/welcome/home')
def welcome_home():
        return "Welcome Home!"

@app.route('/welcome/back')
def Welcome_Back():
        return "Welcome Back!"