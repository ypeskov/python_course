# Run this image by commands:
# To build: docker build -t flask_app .
# To run: docker run -p 5000:5000 flask_app

FROM python:3.9-buster

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY app/ /code/app/

EXPOSE 5000

WORKDIR /code/app

CMD ["python", "app.py"]