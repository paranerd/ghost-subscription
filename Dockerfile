FROM ubuntu:focal

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-urllib3 python3-pip

RUN pip3 install -r requirements.txt

RUN /bin/echo -e '#!/bin/bash\npython3 /app/main.py' > /usr/bin/crawl && \
    chmod +x /usr/bin/crawl
