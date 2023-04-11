FROM python:3.10

LABEL maintainer="WoongSeopOh/Patrick <wsoh@vng.kr>"

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]