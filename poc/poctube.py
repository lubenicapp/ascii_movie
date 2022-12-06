from pytube import YouTube
import os
import time

DIR = './downloads'
EXT = 'mp4'


def download_video(youtube_link):
    video_id = parse_youtube_link(youtube_link)
    target_path = os.path.join(DIR, f'{video_id}.{EXT}')
    if os.path.isfile(target_path):
        print('video already downloaded')
        return target_path
    yt = YouTube(youtube_link)
    yt.streams.filter(file_extension=EXT).first().download(DIR, filename=f'{video_id}.mp4')
    print(f'video downloaded: {target_path}')
    return target_path


def parse_youtube_link(youtube_link):
    video_id = youtube_link.split('v=')[1].split('&')[0]
    return video_id
