FROM python:3
ENV PYTHONUNBUFFERED 1


ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

CMD python3 manage.py runserver 0.0.0.0:8000