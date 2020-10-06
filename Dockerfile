FROM williamlagos/python_vscode:2
RUN python2 manage.py migrate
RUN python2 manage.py collectstatic --noinput
CMD gunicorn --bind 0.0.0.0:$PORT brew.wsgi