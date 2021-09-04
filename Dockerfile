FROM ubuntu:20.04

WORKDIR /app
COPY . .

RUN sudo apt-get install -y build-essential python3-pip
RUN python3 -m pip install --upgrade pip \
    sed -i '1d' requirements.txt \
    python3 -m pip install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 8000
CMD ["bash", "start.sh"]
