import subprocess
import concurrent.futures
from itertools import product

REPOSITORY = "ismailbouajaja"
IMAGE_NAME = "poetry-init"
PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]
PYTHON_TYPES = ["", "-slim"]

def build_and_push_image(image_name: str, tag: str, repository: str, **args: dict[str, str]):
    try:
        # Build the Docker image
        print(f"Building {IMAGE_NAME}:{tag}...")
        args = " ".join([f"--build-arg {key}={value}" for key, value in args.items()])
        build_command = f"docker build {args} -t {image_name}:{tag} ."
        subprocess.run(build_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Tag the Docker image
        tag_command = f"docker tag {image_name}:{tag} {repository}/{image_name}:{tag}"
        subprocess.run(tag_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Push the Docker image
        print(f"Pushing {IMAGE_NAME}:{tag} to {REPOSITORY}...")
        push_command = f"docker push {repository}/{image_name}:{tag}"
        subprocess.run(push_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print(f"Image {IMAGE_NAME}:{tag} successfully built and pushed to {REPOSITORY}...")
    except Exception as e:
        print(f"Error building and pushing image {IMAGE_NAME}:{tag} to {REPOSITORY}: {e}")

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for python_version, python_type in product(PYTHON_VERSIONS, PYTHON_TYPES):
            python_tag = f"{python_version}{python_type}"
            args = {
                "PYTHON_TAG": python_tag,
            }
            tag = python_tag
            future = executor.submit(build_and_push_image, IMAGE_NAME, tag, REPOSITORY, **args)
            futures.append(future)

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
