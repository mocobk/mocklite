FROM python:3.7-alpine
LABEL maintainer="mailmzb@163.com"
ENV TZ="Asia/Shanghai"
ENV FLASK_ENV="production"
WORKDIR /usr/src

# 配置清华镜像地址
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories

# 更新升级软件
RUN apk add --update --upgrade

# 安装软件
RUN apk add --no-cache nginx uwsgi uwsgi-python3

# 替换nginx的配置
COPY nginx.conf /etc/nginx/nginx.conf


# RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
# 以下两句在 COPY . . 之前主要是为了利用 build 缓存，避免每次提交代码都重装 python 依赖
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --timeout 600

COPY . .

CMD nginx -g "daemon on;" && uwsgi --ini uwsgi_config.ini --cache-blocksize 0 && python3 proxy/addon.py