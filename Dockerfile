# syntax=docker/dockerfile:1

# Set the Python version to install
ARG PYTHON_VERSION=3.12-slim

# Use an official Python image
FROM python:${PYTHON_VERSION}

# Set the Poetry version to install
ARG POETRY_VERSION=1.8.*
ARG PYTHONDONTWRITEBYTECODE=1
ARG PYTHONUNBUFFERED=1

# Set environment variables for Python
ENV POETRY_VERSION=${POETRY_VERSION} \
    PYTHONDONTWRITEBYTECODE=${PYTHONDONTWRITEBYTECODE} \
    PYTHONUNBUFFERED=${PYTHONUNBUFFERED}

# Create a directory for the application
WORKDIR /project

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install and configure poetry
RUN pip install "poetry==${POETRY_VERSION}"
RUN poetry config virtualenvs.create false

# Create a script to initialize the Poetry project interactively
ENV PATH="${PATH}:/usr/local/bin"
RUN echo "poetry init" > /usr/local/bin/it && chmod +x /usr/local/bin/it

# Set the entrypoint to run the script
ENTRYPOINT ["bash", "-c"]

# Initialize the Poetry project
CMD ["poetry init --no-interaction"]