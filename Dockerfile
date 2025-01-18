# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS base

# Prevents Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install poetry
ENV POETRY_HOME=/app/poetry
ENV POETRY_VENV=/app/poetry-venv
ENV POETRY_CACHE_DIR=/app/.cache

# Create directories and set permissions
RUN mkdir -p $POETRY_HOME $POETRY_VENV $POETRY_CACHE_DIR \
    && chown -R appuser:appuser /app

# Install poetry separated from system interpreter
RUN python -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry

# Add poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Copy poetry files
COPY --chown=appuser:appuser poetry.lock pyproject.toml ./

# Copy the source code
COPY --chown=appuser:appuser . .

# Switch to non-privileged user
USER appuser

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Expose the port that the application listens on
EXPOSE 8080

# Run the application
CMD ["poetry", "run", "python", "main.py"]
