FROM python:3.7
LABEL maintainer="mailmzb@163.com"
ENV TZ="Asia/Shanghai"
ENV FLASK_ENV="production"

WORKDIR /usr/src

# set -x 可以输入命令信息，方便查看日志
RUN set -x \
    && echo "deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib" > /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian-security stretch/updates main" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian-security stretch/updates main" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib" >> /etc/apt/sources.list \
    && apt update


# 更新升级软件
RUN apt install -y nginx


# 替换nginx的配置
COPY .nginx /etc/nginx/nginx.conf

RUN pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
# 以下两句在 COPY . . 之前主要是为了利用 build 缓存，避免每次提交代码都重装 python 依赖
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --timeout 600

COPY . .

CMD service nginx start && uwsgi -d --ini uwsgi_config.ini --cache-blocksize 0 && python run_proxy.py >> proxy.log