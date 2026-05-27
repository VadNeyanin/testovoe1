FROM ubuntu:22.04@sha256:4f838adc7181d9039ac795a7d0aba05a9bd9ecd480d294483169c5def983b64d

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip=22.0.2+dfsg-1ubuntu0.7 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY /part_1_python /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt
RUN groupadd -r appuser && useradd -r -g appuser -m -s /bin/bash appuser
RUN chown -R appuser:appuser /app && chmod +x /app
USER appuser
CMD ["python3", "/app/main.py"]
