import subprocess
import os

# Configuration
GITHUB_REPO_URL = "https://github.com/RohanRusta21/Weather-App.git"
DOCKER_IMAGE_NAME = "ttl.sh/weather-app-demo"
DOCKER_IMAGE_TAG = "10h"


def checkout_code():
    """Clone the source code from GitHub."""
    print("Cloning repository...")
    if os.path.exists("repository"):
        print("hello repository already existing, removing first before cloning")
        subprocess.run(["rm", "-rf", "repository"], check=True)
    subprocess.run(["git", "clone", GITHUB_REPO_URL, "repository"], check=True)
    print("Repository cloned successfully.")

def build_docker_image():
    """Build a Docker image from the source code."""
    print("Building Docker image...")
    os.chdir("repository")
    if not os.path.exists("Dockerfile"):
        raise Exception("Dockerfile not found in the repository!")
    subprocess.run(["docker", "build", "-t", DOCKER_IMAGE_NAME+":"+DOCKER_IMAGE_TAG,  "."], check=True)
    print(f"Docker image {DOCKER_IMAGE_NAME} built successfully.")

def run_docker_image():
    """Run my Docker image from the source code."""
    print("Running Docker image...")
    subprocess.run(["docker", "run", "-it", "-p", "3011:3000", DOCKER_IMAGE_NAME+":"+DOCKER_IMAGE_TAG], check=True)
    print(f"Docker image {DOCKER_IMAGE_NAME} running successfully.")


def main():
    """Main function to execute the CI/CD pipeline."""
    try:
        # Step 1: Checkout source code
        checkout_code()

        # Step 2: Build Docker image
        build_docker_image()

        # Step 3: Run Docker image
        run_docker_image()

        print("CI/CD pipeline executed successfully!")
    except Exception as e:
        print(f"Pipeline failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()
