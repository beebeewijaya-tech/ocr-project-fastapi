FROM python:3.8-alpine

WORKDIR /usr/src/app

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
RUN apk add --update --no-cache tesseract-ocr

COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./ .

USER 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]