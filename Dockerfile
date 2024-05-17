FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN python scripts/generate_all.py
EXPOSE 8000

CMD ["python", "server.py"]

