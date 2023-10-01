#!/usr/local/bin/python

"A naive script to download music from Youtube as mp3."

import os
import sys
import getopt
from functools import reduce
from pytube import YouTube
from moviepy.editor import AudioFileClip


def convert_to_mp3(input_file, output_directory):
    "Convert a media file to mp3."
    _, file_name = os.path.split(input_file)

    base_name = os.path.splitext(file_name)[0]
    new_file_name = base_name + ".mp3"
    output_file = os.path.join(output_directory, new_file_name)
    with AudioFileClip(input_file) as clip:
        clip.write_audiofile(output_file)
    return output_file


def download_and_convert(link, temporary_path, output_path):
    """
    Download the music at the specified link, convert it to mp3 format
      and save it to the specified output path.
    """
    try:
        youtube_object = YouTube(link)
        # title = youtube_object.title
        youtube_stream = (
            youtube_object.streams.filter(only_audio=True)
            .order_by("abr")
            .desc()
            .first()
        )

        temporary_file = youtube_stream.download(
            output_path=temporary_path, filename=youtube_stream.default_filename
        )
    except Exception:
        print("   An error has occurred while downloading the file from YouTube")
        return None

    saved_file = convert_to_mp3(temporary_file, output_path)
    os.remove(temporary_file)

    print("   Download is completed successfully")
    return saved_file


def main(argv):
    "The program's entry point"

    inputfile = ""
    output_directory = ""
    temporary_directory = ""
    opts, _ = getopt.getopt(argv, "hi:o:t:", ["ifile=", "odir=", "tdir="])
    for opt, arg in opts:
        if opt == "-h":
            print("test.py -i <inputfile> -o <output_directory>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--odir"):
            output_directory = arg
        elif opt in ("-t", "--tdir"):
            temporary_directory = arg
    print("Input file is: ", inputfile)
    print("Output directory is: ", output_directory)
    print("Temporary directory is: ", temporary_directory)

    with open(inputfile, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        filtered_lines = filter(
            lambda line: (len(line) > 0) and (not line.startswith("#")), lines
        )
        distinct_lines = reduce(
            lambda x, y: x + [y] if y not in x else x, filtered_lines, []
        )

        for line in distinct_lines:
            print(f"Downloading {line}...")
            saved_file = download_and_convert(
                line, temporary_directory, output_directory
            )
            if saved_file is None:
                print("   ... error while saving file.")
            else:
                print(f"   ... done ({saved_file}).")


if __name__ == "__main__":
    main(sys.argv[1:])
