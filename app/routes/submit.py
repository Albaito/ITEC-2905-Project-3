from datetime import datetime
from app import app, db
from flask import redirect, request,url_for
from ..models import Bookmark

@app.route('/submit', methods=['POST'])
def submit():
    location = request.form.get('location')
    date_str = request.form.get('date')

    # Convert the date string to a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')

    # Create a new Bookmark instance
    new_bookmark = Bookmark(location=location, date=date)

    # Add the new bookmark to the database
    db.session.add(new_bookmark)
    db.session.commit()

    # Redirect to results_screen with query parameters
    return redirect(url_for('results_screen', location=location, date=date_str))
