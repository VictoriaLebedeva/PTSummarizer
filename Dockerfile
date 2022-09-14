FROM python:3.10.7-slim-buster

RUN pip install poetry

WORKDIR "/src"

COPY ["poetry.lock", "pyproject.toml", "./"]

RUN poetry install --no-interaction --no-ansi
COPY . .

EXPOSE 9696

ENTRYPOINT  ["poetry", "run", "app" ] 