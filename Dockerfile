FROM python:3.10-bullseye

ADD ./simple-webapp/requirements.txt /tmp/requirements.txt

RUN python3.10 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN python3.10 -m pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD ./simple-webapp /opt/simple-webapp

WORKDIR /opt/simple-webapp

EXPOSE 5000

CMD [ "python", "app.py" ]