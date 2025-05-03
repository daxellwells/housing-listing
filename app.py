from flask import Flask, request, jsonify, render_template
from validate import validate_listing
from database import Database

# initiates the database
db = Database()

app = Flask(__name__)

# renders the submission page
@app.route('/submit-form', methods=["GET"])
def get_page():
    return render_template('submit.html')

# submits listing into database
@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.form)
    #v alidates submission: if invalid, returns an error
    validation, message = validate_listing(data)
    if not validation:
        return message, 400
    db.insert_listing(data)
    return render_template("submitted.html")

# renders the listings page; creates a table for all listings in the database
@app.route('/listings', methods=['GET'])
def get_listings():
    listings = db.get_all_listings()
    return render_template('listings.html', listings=listings)