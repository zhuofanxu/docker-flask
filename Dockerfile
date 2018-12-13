FROM python:3.6-alpine

# 创建并使用非 root 用户
# RUN addgroup -S gunicorn && adduser -S -G gunicorn gunicorn
# USER gunicorn

# 环境变量
ENV PYTHONUNBUFFERED 1

# 创建并指定工作目录
RUN mkdir -p /home/gunicorn
WORKDIR /home/gunicorn

COPY web/requirements ./

# 安装应用依赖
# First installing client libraries and any other package we need
# Then installing build dependencies
RUN apk update && apk add libpq \
    && apk add --no-cache --virtual .build-deps \ 
    gcc \
    libffi-dev \
    libc-dev \
    libevent-dev \
    python3-dev \
    musl-dev \
    postgresql-dev \
    make \
    git \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements \
    && apk del --no-cache .build-deps

# Last clear build dependencies

#USER gunicorn

# COPY 比 ADD指令更透明 优先使用
# ADD 的最佳用例是将本地 tar 文件自动提取到镜像中，例如 ADD rootfs.tar.xz
COPY . .

# 曝露端口
EXPOSE 8000

# 启动服务
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--chdir", "web", "wsgi:application"]