FROM python:3.9

ENV DockerHOME=/home/Desktop/Zadanie1/mysite

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pi

COPY . $DockerHOME
RUN pip install -r requirements.txt

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
