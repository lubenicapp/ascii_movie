#!/usr/bin/env python3

import argparse
import os
from poc.poctube import download_video
from poc.asciify import asciify_image
import imageio.v3 as iio
import time

parser = argparse.ArgumentParser()
parser.add_argument("youtube")
args = parser.parse_args()

FRAME_RATE = 24


def run(youtube_link, lines, columns):
    video_path = download_video(youtube_link)
    print(video_path)
    ascii_images = []
    frames = iio.imread(video_path, plugin="pyav")
    print(f"{len(frames)} frames to process... ")
    for frame in frames:
        ascii_images.append(asciify_image(frame, lines, columns))
    for image in ascii_images:
        print(image)
        time.sleep(1/FRAME_RATE)


if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    terminal_h, terminal_w = terminal_size.lines, terminal_size.columns

    run(args.youtube, terminal_h, terminal_w)
