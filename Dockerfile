FROM williamlagos/python_vscode:2

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python2 -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

# EXPOSE 8000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
RUN python2 manage.py collectstatic --noinput
CMD gunicorn --bind 0.0.0.0:$PORT brew.wsgi 
