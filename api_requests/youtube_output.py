"""This file processes the result from the YOuTube API """

from youtubeApiExample import city_video


# getting data, extract data, return data
# first_result = search_response.get('items', [])[0]
def get_video_title(first_result):
    title = first_result['snippet']['title']
    return title


def get_video_id(first_result):
    video_id = "(null)"
    if 'videoId' in first_result['id']:           # return video
        video_id = first_result['id']['videoId']
    elif 'channelId' in first_result['snippet']:
        video_id = first_result['snippet']['channelId']
    return video_id


def get_youtube_video(city):
        first_result = city_video(city)
        title = get_video_title(first_result)
        videoID = get_video_id(first_result)
        return title,videoID
"""@Adade Gbadoe
 Here’s what we talked about: Make a file called youtube_output.py
  that returns the video title and video ID from the YouTube API. 
  You can look at my climate_output.py and poi_output.py files for reference. 
 Your file should do the same thing as those, but using your YouTube API."""