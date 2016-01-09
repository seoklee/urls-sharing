from flask import Flask

# creating the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=False)

import views
