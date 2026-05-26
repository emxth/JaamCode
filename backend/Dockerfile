FROM python:3.12-slim

WORKDIR /app

ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Copy dependency manifests first for caching
COPY pyproject.toml uv.lock* /app/

# Install uv + deps
RUN pip install --no-cache-dir uv \
  && uv sync --frozen --dev

# Copy backend code
COPY . /app

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]