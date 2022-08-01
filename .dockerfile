# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR .

RUN sudo apt-get install libcairo2-dev

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "main" ]
