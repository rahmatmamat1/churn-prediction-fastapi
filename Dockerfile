FROM python:3.9-slim
# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["model_C=1.0.bin", "predict_fastapi.py", "./"]

RUN pip install gunicorn

# EXPOSE 9696

# ENTRYPOINT [ "python", "predict_fastapi.py" ]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --worker-class uvicorn.workers.UvicornWorker --timeout 0 predict_fastapi:app