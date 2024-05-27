import subprocess
import concurrent.futures

REPOSITORY = "ismailbouajaja"
IMAGE_NAME = "poetry-init"
TAGS_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]
TAGS_FAMILIES = ["", "-slim"]

def build_and_push_image(image_name: str, tag: str, repository: str):
    # Build the Docker image
    print(f"Building {IMAGE_NAME}:{tag}...")
    build_command = f"docker build --build-arg PYTHON_VERSION={tag} -t {image_name}:{tag} ."
    subprocess.run(build_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Tag the Docker image
    tag_command = f"docker tag {image_name}:{tag} {repository}/{image_name}:{tag}"
    subprocess.run(tag_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Push the Docker image
    print(f"Pushing {IMAGE_NAME}:{tag} to {REPOSITORY}...")
    push_command = f"docker push {repository}/{image_name}:{tag}"
    subprocess.run(push_command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"Image {IMAGE_NAME}:{tag} successfully built and pushed to {REPOSITORY}...")

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for version in TAGS_VERSIONS:
            for family in TAGS_FAMILIES:
                tag = f"{version}{family}"
                future = executor.submit(build_and_push_image, IMAGE_NAME, tag, REPOSITORY)
                futures.append(future)

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
