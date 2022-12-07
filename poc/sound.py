import os
import pathlib
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pydub.playback import play
import threading


def mp4_to_mp3(video_path):
    video = VideoFileClip(video_path)
    sound_path = os.path.join(os.path.dirname(video_path), f'{pathlib.Path(video_path).stem}.wav')
    video.audio.write_audiofile(sound_path)
    return sound_path


def play_mp3(audio_path):
    song = AudioSegment.from_wav(audio_path)
    play(song)


def start_play_thread(audio_path):
    x = threading.Thread(target=play_mp3, args=[audio_path])
    x.start()


def play_audio_from_video(video_path):
    start_play_thread(mp4_to_mp3(video_path))
