FROM python:3.7
LABEL maintainer="mailmzb@163.com"
ENV TZ="Asia/Shanghai"
ENV FLASK_ENV="production"

WORKDIR /usr/src


# 更新升级软件
RUN apt -y update && apt install nginx


# 替换nginx的配置
COPY nginx.conf /etc/nginx/nginx.conf

RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
# 以下两句在 COPY . . 之前主要是为了利用 build 缓存，避免每次提交代码都重装 python 依赖
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --timeout 600

COPY . .

CMD nginx -g "daemon on;" && uwsgi --ini uwsgi_config.ini --cache-blocksize 0 && python3 proxy/addon.py