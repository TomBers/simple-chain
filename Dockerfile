FROM python:3.11-slim

RUN pip install poetry==1.6.1

RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml ./README.md ./poetry.lock* ./

COPY ./packages ./packages

RUN poetry install  --no-interaction --no-ansi --no-root

COPY ./app ./app

COPY ./static ./static

# Set environment variables
# ON FLY.io - flyctl secrets set OPENAI_API_KEY="YOUR_API_KEY"
# COPY ./.env ./.env

COPY ./simple_chain.py ./simple_chain.py

RUN poetry install --no-interaction --no-ansi

EXPOSE 8080

CMD exec uvicorn app.server:app --host 0.0.0.0 --port 8080
