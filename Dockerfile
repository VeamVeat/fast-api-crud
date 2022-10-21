FROM python:3.10

WORKDIR /fast_api_crud

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install netcat -y && \
    apt-get install postgresql gcc python3-dev musl-dev -y && \
    pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt

RUN ["chmod", "+x", "/fast_api_crud/entrypoint.sh"]

ENTRYPOINT ["/fast_api_crud/entrypoint.sh"]
