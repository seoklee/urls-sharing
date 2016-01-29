from flask import Flask
from flask_wtf.csrf import CsrfProtect

# creating the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=False)
CsrfProtect(app)

import views
