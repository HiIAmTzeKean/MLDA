import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True,
            template_folder='templates')


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/')
def index():
    return "hello world"
