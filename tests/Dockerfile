
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

RUN pip install selenium pytest

WORKDIR /app

COPY test_site.py .

CMD ["pytest", "-v", "test_site.py"]
