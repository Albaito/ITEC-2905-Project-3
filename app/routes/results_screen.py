from app import app
from flask import render_template, request
from ..api_requests import *
import json

@app.route('/results_screen')
def results_screen():
    location = request.args.get('location')
    date_str = request.args.get('date')
    climate_data = climate_api.request_climate(location, date_str)
    pio_data = poi_api.request_poi(location)
    youtube_videos_data = youtubeApiExample.city_video(location)
    
    if isinstance(youtube_videos_data, dict):
        youtube_videos = [youtube_videos_data]
    else:
        try:
            youtube_videos = json.loads(youtube_videos_data)
        except json.JSONDecodeError:
            print(f"Failed to decode JSON: {youtube_videos_data}")
            youtube_videos = []

    print(youtube_videos[0]['id'])

    return render_template('results_screen.html', location=location, date=date_str, climate_data=climate_data, pio_data=pio_data, youtube_videos=youtube_videos)
