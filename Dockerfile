FROM python:3.10
WORKDIR /bot
COPY requirements.txt /bot/
RUN apt-get update && \
    apt-get install -y build-essential libatlas-base-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /bot
CMD ["sh", "-c", "cd src && python3 main.py"]