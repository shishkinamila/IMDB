FROM python:3.8-slim-buster

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt && pytest test.py
CMD [ "python3", "imdb.py"]
