FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm ./requirements.txt

COPY ./download_mp3_from_youtube.py .

ENTRYPOINT ["python", "./download_mp3_from_youtube.py"]


# Build:
# 	docker build -t download_mp3_from_youtube -f ./Dockerfile .
#
# Run:
#	docker run -it --rm -v ${PWD}:/input -v ${home}/music:/output download_mp3_from_youtube -i /input/my_play_list.txt -o /output