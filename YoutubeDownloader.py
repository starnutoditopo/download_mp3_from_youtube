#!/usr/local/bin/python

from pytube import YouTube
import sys, getopt

def Download(link, output_path):
    saved_file = None
    try:
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.filter(only_audio=True).first()
        saved_file = youtube_object.download(output_path=output_path)
    except Exception:
        print("   An error has occurred")
        return

    print("   Download is completed successfully")
    return saved_file

def main(argv):
    inputfile = ''
    output_directory = ''
    opts, _ = getopt.getopt(argv,"hi:o:",["ifile=","odir="])
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <output_directory>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--odir"):
            output_directory = arg
    print ('Input file is: ', inputfile)
    print ('Output directory is: ', output_directory)

    with open(inputfile, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
        for line in lines:
            link = line.strip()
            if len(link) == 0 or link.startswith('#'):
                continue
            print(f'Downloading {link}...')
            saved_file = Download(link, output_directory)
            print(f'   ... done ({saved_file}).')

if __name__ == '__main__':
    main(sys.argv[1:])