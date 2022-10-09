FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
# WORKDIR /app

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["model_C=1.0.bin", "predict_fastapi.py", "./"]

RUN pip install gunicorn

# EXPOSE 9696

# ENTRYPOINT [ "waitress-serve", "--listen=0.0.0.0:9696", "predict_fastapi:app" ]
# ENTRYPOINT [ "python", "predict_fastapi.py" ]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 predict_fastapi:app 

# Copy local code to the container image.
# ENV APP_HOME /app
# WORKDIR $APP_HOME
# COPY . ./

# Install production dependencies.
# RUN pip install --no-cache-dir -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app