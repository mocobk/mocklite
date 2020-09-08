FROM python:3.7-alpine
LABEL maintainer="mailmzb@163.com"
ENV TZ="Asia/Shanghai"
ENV FLASK_ENV="production"
ENV REPOSITORY_MAIN="https://mirrors.aliyun.com/alpine/latest-stable/main"
WORKDIR /usr/src


# 更新升级软件
RUN apk add --update --upgrade


# 编译 uwsgi所需包：gcc libc-dev linux-headers
# 编译 lxml所需包：gcc libc-dev linux-headers
# gcc 包相对较大 90+M
# date 默认 UTC， 需添加 tzdata 设置时区，并添加 TZ 环境变量
RUN echo ${REPOSITORY_MAIN} > /etc/apk/repositories \
    && apk add --no-cache gcc musl-dev libxslt-dev libc-dev libffi-dev libressl-dev linux-headers tzdata nginx \
    && cp /usr/share/zoneinfo/${TZ} /etc/lcoaltime \
    && echo ${TZ} > /etc/timezone

# 替换nginx的配置
COPY nginx.conf /etc/nginx/nginx.conf

RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
# 以下两句在 COPY . . 之前主要是为了利用 build 缓存，避免每次提交代码都重装 python 依赖
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --timeout 600

COPY . .

CMD nginx -g "daemon on;" && uwsgi --ini uwsgi_config.ini --cache-blocksize 0 && python3 proxy/addon.py