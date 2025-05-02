from flask import Flask, request
from validate import validate_listing
from database import Database

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.form)
    validation = validate_listing(data)
    if not validation[0]:
        return validation[1], 400
