# syntax=docker/dockerfile:1

# Set the Poetry version to install
ARG POETRY_VERSION=1.8

# Set the Python version to install
ARG PYTHON_TAG=3.10-slim

# Use a poetry image with the specified version
FROM ismailbouajaja/poetry:poetry__${POETRY_VERSION}--python__${PYTHON_TAG}

# Create a directory for the application
WORKDIR /target

# Create a script to initialize the Poetry project interactively
ENV PATH="${PATH}:/usr/local/bin"
RUN echo "poetry init" > /usr/local/bin/it && chmod +x /usr/local/bin/it

# Set the entrypoint to run the script
ENTRYPOINT ["/usr/local/bin/base-entrypoint.sh", "bash", "-c"]

# Initialize the Poetry project
CMD ["poetry init --no-interaction"]