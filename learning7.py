import os

image_name = 'myapp:latest'
dockerhub_repo = 'username/myapp'

os.system(f'docker build -t {image_name} .')
os.system(f'docker tag {image_name} {dockerhub_repo}')
os.system(f'docker push {dockerhub_repo}')