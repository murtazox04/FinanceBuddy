FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create directory for gunicorn logs
RUN mkdir -p /var/log/gunicorn

# Copy gunicorn config
COPY gunicorn_config.py .

# Run with gunicorn
CMD ["gunicorn", "core.asgi:application", "-c", "gunicorn_config.py"]
