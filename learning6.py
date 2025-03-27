import subprocess
import sys

# Configuration
GIT_REPO_URL = "https://github.com/your-username/your-repo.git"
CLONE_DIR = "app"
DOCKER_IMAGE_NAME = "myapp:latest"
CONTAINER_NAME = "myapp_container"

def run_cmd(command, cwd=None):
    try:
        result = subprocess.run(command, cwd=cwd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        sys.exit(1)

def clone_repo():
    print("[+] Cloning Git repo...")
    run_cmd(f"git clone {GIT_REPO_URL} {CLONE_DIR}")

def build_docker_image():
    print("[+] Building Docker image...")
    run_cmd(f"docker build -t {DOCKER_IMAGE_NAME} .", cwd=CLONE_DIR)

def run_docker_container():
    print("[+] Running Docker container...")
    run_cmd(f"docker rm -f {CONTAINER_NAME}", cwd=CLONE_DIR)  # Remove existing container if exists
    run_cmd(f"docker run -d --name {CONTAINER_NAME} -p 80:80 {DOCKER_IMAGE_NAME}", cwd=CLONE_DIR)

if __name__ == "__main__":
    clone_repo()
    build_docker_image()
    run_docker_container()
    print("[✓] Deployment complete!")