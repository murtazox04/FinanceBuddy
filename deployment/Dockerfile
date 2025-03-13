# Build stage
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    gettext \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install gunicorn uvicorn

# Final stage
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gettext \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn

# Copy application code
COPY . /app/

# Create non-root user
RUN addgroup --system django \
    && adduser --system --ingroup django django \
    && mkdir -p /app/staticfiles /app/media \
    && chown -R django:django /app

USER django

RUN python manage.py collectstatic --noinput

EXPOSE 8004

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "core.asgi:application", "--bind", "0.0.0.0:8004"]