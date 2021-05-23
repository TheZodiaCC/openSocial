FROM python:3.8.5

COPY . /openSocial

WORKDIR /openSocial

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]