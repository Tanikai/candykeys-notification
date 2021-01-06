FROM python:3.8-slim-buster

# App directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

CMD [ "python", "./service.py" ]
