""" This file present the user interface for getting YouTube video information"""

from .youtube_output import get_youtube_video

if __name__ == '__main__':        # this calls main function
    city = input("Which city: ")
    title, videoID = get_youtube_video(city)
    print(f'Title: "{title}"\nID: {videoID}')
