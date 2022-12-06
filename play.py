#!/usr/bin/env python3

import argparse
import cv2
import os
from poc.poctube import download_video
from poc.asciify import asciify_image
import imageio.v3 as iio
from time import time, sleep

parser = argparse.ArgumentParser()
parser.add_argument("youtube")
args = parser.parse_args()


def play(youtube_link, lines, columns):
    video_path = download_video(youtube_link)
    print(video_path)
    frame_rate = cv2.VideoCapture(video_path).get(cv2.CAP_PROP_FPS)

    frames = iio.imread(video_path, plugin="pyav")
    print(f"{len(frames)} frames to process... ")

    start = time()
    ascii_images = [asciify_image(frame, lines, columns) for frame in frames]
    end = time()

    for image in ascii_images:
        print(image)
        sleep(1/frame_rate)
    print(f'duration: {round(end-start)} seconds')


if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    terminal_h, terminal_w = terminal_size.lines, terminal_size.columns

    play(args.youtube, terminal_h, terminal_w)
