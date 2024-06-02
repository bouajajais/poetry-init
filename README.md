# poetry-init

A docker image for initializing a python project using `poetry init`.

## Available tags

Tags reflect the image of python used and the version of poetry installed on top.

Tags follow this format : `${POETRY_VERSION}-python${PYTHON_TAG}`.

Currently, `latest` corresponds to `1.8-python3.12-slim`.

Here are the TAGS currently available :
```Python
POETRY_VERSIONS = ["1.6", "1.7", "1.8"]
PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]
PYTHON_TYPES = ["", "-slim"]
```

Other tags will be added later.

## Usage

You may run it directly from Docker Hub or by cloning the github repository and building the image locally before running it.

### Using Docker Hub image

To use the `poetry-init` image from Docker Hub, run the following command :

```bash
docker run --rm -u $(id -u):$(id -g) -v /path/to/project:/target ismailbouajaja/poetry-init
```

This is equivalent to `poetry init --no-interaction`.

OR run it interactively with the following command :

```bash
docker run --rm -it -u $(id -u):$(id -g) -v /path/to/project:/target ismailbouajaja/poetry-init it
```

This is equivalent to `poetry init`.

## Clone repository

To clone the github repository containing the Dockerfile used, follow these steps :

1. Clone the repository:
    ```bash
    git clone https://github.com/bouajajais/poetry-init.git
    ```

2. Navigate to the project directory:
    ```bash
    cd poetry-init
    ```

2. Build the Docker image using the provided Dockerfile:
    ```bash
    docker build -t poetry-init .
    ```

    The `docker build` command accepts the following arguments:
    - `ARG PYTHON_TAG=3.12-slim`: The Python base image tag.
    - `ARG POETRY_VERSION=1.8`: The Poetry version to install.
    - `ARG PYTHONDONTWRITEBYTECODE=1`: Other argument.
    - `ARG PYTHONUNBUFFERED=1`: Other argument.

3. Run the Docker container, passing the desired volume path as an argument:
    This will initialize a new Python project at the specified path.

    ```bash
    docker run --rm -u $(id -u):$(id -g) -v /path/to/project:/target poetry-init
    ```

    This is equivalent to `poetry init --no-interaction`.

    OR run it interactively with

    ```bash
    docker run --rm -it -u $(id -u):$(id -g) -v /path/to/project:/target poetry-init it
    ```

    This is equivalent to `poetry init`.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.