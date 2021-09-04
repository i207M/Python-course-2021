FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN apt-get update

RUN python -m pip install --upgrade pip && \
    sed -i '1d' requirements.txt && \
    python -m pip install -r requirements.txt
RUN chmod +x start.sh

EXPOSE 8000
CMD ["bash", "start.sh"]
