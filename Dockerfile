# 使用官方的 Python 基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将当前目录下的文件复制到容器中的/app目录
COPY . /app

# 安装项目所需的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 运行 Flask 应用
CMD ["flask", "run"]
