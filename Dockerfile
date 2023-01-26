FROM python:3.9.14

WORKDIR /app
COPY ./birdie/requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./birdie/*.* .
RUN chown -R nobody /app
USER nobody
ENV BOT_TOKEN=change_me

ENTRYPOINT ["python3", "bot.py"]
