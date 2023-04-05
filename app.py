from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Cauê - RA: 2103161\nGustavo - RA:\nWelisson - RA:'