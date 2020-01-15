FROM python:3
RUN mkdir /src
WORKDIR /code
COPY tracker.py /src/tracker.py
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
EXPOSE 8086
COPY . /src/