FROM python:3.9.4

WORKDIR /opt/App

ADD ./App /opt/App

RUN pip install --upgrade pip
RUN pip install -r /opt/App/requirements.txt

RUN chmod +x /opt/App/run.sh

EXPOSE 8001

CMD ["bash", "./run.sh"]