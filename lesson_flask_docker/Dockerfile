FROM python:3.9.2-buster

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY ./app/ /app

EXPOSE 5000

WORKDIR /app

CMD ["python", "app.py"]