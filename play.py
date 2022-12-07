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
    frame_rate = cv2.VideoCapture(video_path).get(cv2.CAP_PROP_FPS)

    frames = iio.imread(video_path, plugin="pyav")
    print(f"{len(frames)} frames to process... ")

    start = time()
    for i, frame in enumerate(frames):
        if frame_is_late(start, i, frame_rate):
            continue
        img = asciify_image(frame, lines, columns)
        while not frame_is_late(start, i, frame_rate):
            sleep(1 / (10 * frame_rate))
        print(img)


def frame_is_late(start, frame_number, frame_rate):
    return time() - start > frame_number * (1 / frame_rate)

if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    terminal_h, terminal_w = terminal_size.lines, terminal_size.columns

    play(args.youtube, terminal_h, terminal_w)
