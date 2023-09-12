#!/usr/local/bin/python
from pytube import YouTube
import os

def Download(link, output_path):
    try:
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.filter(only_audio=True).first()
        #destination = os.path.join(output_path, f'{youtube_object.title}.mp3')
        #youtube_object.download(output_path=destination)
        youtube_object.download(output_path=output_path)
    except Exception:
        print("An error has occurred")
        return
    
    print("Download is completed successfully")

def main():
    output_path = './output'
    links = [
        # 'https://youtu.be/lWA2pjMjpBs',
        # 'https://youtu.be/kJQP7kiw5Fk',
        # 'https://youtu.be/HCjNJDNzw8Y',
        # 'https://youtu.be/DeumyOzKqgI',
        # 'https://youtu.be/Bg3pFjbCag0',
        # 'https://youtu.be/rRzJq9GvUjY',
        # 'https://youtu.be/9jK-NcRmVcw',
        # 'https://youtu.be/eErgDjAOyz8',
        # 'https://youtu.be/QkF3oxziUI4',
        # 'https://youtu.be/uSiHqxgE2d0',
        # 'https://youtu.be/6xULwPM--KY',
        # 'https://youtu.be/jx8GhXm-HcA',
        # 'https://youtu.be/ccqcpOLaMk8',
        # 'https://youtu.be/2tkEi1aSOYg',
        # 'https://youtu.be/kyxEpZfh4iA',
        # 'https://youtu.be/wKvJHFy5kHo',
        # 'https://youtu.be/09vV1WSJzVs',
        # 'https://youtu.be/RlxAhvi-j_U',
        # 'https://youtu.be/PZMJAkSLa0o',
        # 'https://youtu.be/faL2qm-F1jM',
        # 'https://youtu.be/eMnxjdGTK4w',
        # 'https://youtu.be/k1tyVlKjJZI',
        # 'https://youtu.be/68ugkg9RePc',
        # 'https://youtu.be/fPO76Jlnz6c',
        # 'https://youtu.be/1V_xRb0x9aw',
        # 'https://youtu.be/6qXLem0_mRc',
        # 'https://youtu.be/k9qUvf8j5Dc'
        # 'https://youtu.be/0J2QdDbelmY'
        # 'https://youtu.be/2wUvlTUi8kQ',
        # 'https://youtu.be/WZ32gSLNHfA',
        # 'https://youtu.be/4E-1rkj60Z0',
        # 'https://youtu.be/jcmdzOcyb0w',
        # 'https://youtu.be/13U43P_dsQ4',
        # 'https://youtu.be/lN5wpoNJDUk',
        # 'https://youtu.be/wd9r0xTGhyo',
        # 'https://youtu.be/n7C1tOOJpsk',
        # 'https://youtu.be/6Ejga4kJUts',
        # 'https://youtu.be/8Dd-wDxT07Y',
        # 'https://youtu.be/IVqnx1LAh7s'
    ]
    for link in links:
        Download(link, output_path)

if __name__ == '__main__':
    main()