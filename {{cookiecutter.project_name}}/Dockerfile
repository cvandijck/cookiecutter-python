FROM python:{{ cookiecutter.minimal_python_version }}

WORKDIR /app

RUN apt-get update && apt-get install -y

ADD ./src ./src
ADD ./app ./app

RUN pip install -U pip wheel -r ./app/requirements.txt

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

ENTRYPOINT ["python", "./app/app.py"]