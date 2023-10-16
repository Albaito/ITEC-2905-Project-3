# Get a cities video from YouTube.
# Set the YOUTUBE_API_KEY as an environment variable

# Helpful Google example: https://github.com/youtube/api-samples/blob/master/python/search.py

# Need the video title. Also the video ID for building a URL to embed the video in a home_page
# https://developers.google.com/youtube/player_parameters
from pprint import pprint
from googleapiclient.discovery import build  # install wrapper library that make AII call to Google APIs
# allows connections to multiple google products and service: map, places, google translate, youtube....
from googleapiclient.errors import HttpError

import os  # It allows connection to my computer: it has method to read the read environment variable

# that my pc stores
# allow python to talk to my windows
DEVELOPER_KEY = os.environ['YOUTUBE_API_KEY']  # API key stored in an environment variable called YOUTBE_API_KEY

YOUTUBE_API_SERVICE_NAME = 'youtube'  # in this program we specifically want youtube
YOUTUBE_API_VERSION = 'v3'


def city_video(category):
    try:
        # build function imported from google client library. IT uses YouTube, version 3, the API_KEY
        # https://googleapis.github.io/google-api-python-client/docs/start.html for documentation
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)  # import

        search_response = youtube.search().list(
            q='cities,' + category,
            part='id, snippet',
            maxResults=1,
            type='videos',
            safeSearch='strict'
        ).execute()

        pprint(search_response)

        # getting data, extract data, retun data
        first_result = search_response.get('items', [])[0]

        title = first_result['snippet']['title']
        video_id = first_result['id']['videoId']

        # https://www.youtube.com/watch?v=6Uxxe2o_n0A
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        print(video_url)

        return {'title': title, 'video_id': video_id}


    except Exception as e:
        print(e)


if __name__ == '__main__':        # this calls main function
    print(city_video('cities'))
