FROM python:3.11.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "python", "app.py" ]


# kubectl port-forward service/sunrise-service 8000:8000
