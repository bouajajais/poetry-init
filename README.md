# poetry-init

This Docker image is built on top of the `ismailbouajaja/poetry` image.

It installs the following element(s) on top:



## Tag Format

Tags follow this format : `poetry__{POETRY_VERSION}--python__{PYTHON_TAG}`.

## Dockerhub

These images can be found in Dockerhub through the following link:

[https://hub.docker.com/repository/docker/ismailbouajaja/poetry-init/general](https://hub.docker.com/repository/docker/ismailbouajaja/poetry-init/general)

## Clone repository

To clone the github repository containing the Dockerfile used, follow these steps :

1. Clone the repository [https://github.com/bouajajais/poetry-init.git](https://github.com/bouajajais/poetry-init.git):
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
    - `ARG POETRY_VERSION=1.8.*`: The Poetry version to install.
    - `ARG PYTHON_TAG=3.12-slim`: The Python base image tag.
    
## Usage

Run the Docker container, passing the desired volume path as an argument:

This will initialize a new `poetry` project at the specified path.

```bash
docker run --rm -e USER_UID=$(id -u) -e USER_GID=$(id -g) -v /path/to/project:/target ismailbouajaja/poetry-init
```

This is equivalent to `poetry init --no-interaction`.

OR run it interactively with

```bash
docker run --rm -it -e USER_UID=$(id -u) -e USER_GID=$(id -g) -v /path/to/project:/target ismailbouajaja/poetry-init it
```

This is equivalent to `poetry init`.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.