# syntax=docker/dockerfile:1

# Set the Python version to install
ARG PYTHON_TAG=3.12-slim

# Set the Poetry version to install
ARG POETRY_VERSION=1.8

# Use an official Python image
FROM ismailbouajaja/poetry:${POETRY_VERSION}-python${PYTHON_TAG}

# Create a directory for the application
WORKDIR /target

# Create a script to initialize the Poetry project interactively
ENV PATH="${PATH}:/usr/local/bin"
RUN echo "poetry init" > /usr/local/bin/it && chmod +x /usr/local/bin/it

# Set the entrypoint to run the script
ENTRYPOINT ["bash", "-c"]

# Initialize the Poetry project
CMD ["poetry init --no-interaction"]