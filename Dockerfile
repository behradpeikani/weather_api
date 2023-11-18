FROM python:latest

WORKDIR /weatherapi

COPY requirements.txt /weatherapi/

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /weatherapi

EXPOSE 8000

CMD ["gunicorn", "core.wsgi", ":8000"]