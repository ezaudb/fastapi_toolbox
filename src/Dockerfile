FROM python:3.12-slim

WORKDIR /my_project

COPY . .

RUN apt-get update && apt-get install -y bash

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/bin/bash"]
