#!/usr/local/bin/python

from pytube import YouTube
import sys, getopt

def Download(link, output_path):
    try:
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.filter(only_audio=True).first()
        youtube_object.download(output_path=output_path)
    except Exception:
        print("   An error has occurred")
        return
    
    print("   Download is completed successfully")

def main(argv):
    inputfile = ''
    output_directory = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","odir="])
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

    output_path = './output'
    
    file = open(inputfile, 'r')
    lines = file.readlines()
    for line in lines:
        link = line.strip()
        if len(link) != 0:
            print(f'Downloading {link}...')
            Download(link, output_path)
            print(f'   ... done.')

if __name__ == '__main__':
    main(sys.argv[1:])