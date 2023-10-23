from app import app
from flask import render_template
from ..models import Bookmark

@app.route('/view_bookmark')
def view_bookmark():
    # Fetch all bookmarks from the database
    bookmarks = Bookmark.query.all()

    # Pass the bookmarks to the template
    return render_template('view_bookmark.html', bookmarks=bookmarks)
