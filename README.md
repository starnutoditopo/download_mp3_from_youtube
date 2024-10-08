This repository has been archived due to changes in youtube, that caused "pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple".
I don't use this tool any more; switched to https://github.com/yt-dlp/yt-dlp, instead.

# Download music resources from Youtube, convert them to mp3 and save them locally.

A python script to batch download audio files from YouTube.

Read the list of media to download from a text file containing a URL per line:

```text
https://youtu.be/lWA2pjMjpBs
https://youtu.be/boaJCrHNRMA?feature=shared
https://youtu.be/NMVYrVBXOfw?feature=shared&t=20
...
```

For each required media, the one with highest audio bit rate is downloaded, converted to mp3 and saved locally.

# Quick start...

## ... with Docker

Edit a text file (eg.: `my_play_list.txt`), so that it contains a YouTube URL for each line (empty lines are ignored, as well as lines starting with '#').

Build the docker image:

```shell
docker build -t download_mp3_from_youtube -f ./Dockerfile .
```shell

Run the following command (Powershell on Windows):

```shell
docker run -it --rm -v ${PWD}:/input -v ${home}/music:/output download_mp3_from_youtube -i /input/my_play_list.txt -o /output
```

Find your .mp3 files in your `Musinc` folder.

## ... running and debugging with Visual Studio Code and Docker

Open this repository as container in Visual Studio Code.

Edit a text file (eg.: `my_play_list.txt`), so that it contains a YouTube URL for each line (empty lines are ignored, as well as lines starting with '#').

Just press **F5**, or run `python download_mp3_from_youtube.py -i <inputFile> -o <outputDirectory>`; example:

```bash
python download_mp3_from_youtube.py -i my_play_list.txt -o ./output
```

Find the downloaded files in the `<outputDirectory>` folder.

# Develop and debug in Visual Studio code in a Docker container

Just open this folder as a Docker container in Visual Studio Code; press F5 to start debugging.
