from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Cauê - RA: 2103161 | Gustavo - RA: 2200299 | Welisson - RA: 2200501'