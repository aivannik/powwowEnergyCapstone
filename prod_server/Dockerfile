FROM python:3.6.3


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /usr/src/app

CMD ["python", "manage.py", "runserver"]