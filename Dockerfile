FROM python:3-alpine
COPY app app
WORKDIR /app
ENTRYPOINT ["./init_processor.sh"]
