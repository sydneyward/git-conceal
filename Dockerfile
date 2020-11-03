FROM python:3-alpine
COPY . .
RUN ["python3", "-m", "unittest", "discover"]

FROM python:3-alpine
COPY --from=0 /app /app
WORKDIR /app
ENTRYPOINT ["./init_processor.sh"]
