FROM python:3.9

RUN mkdir /site

COPY . /site/

WORKDIR /site

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
