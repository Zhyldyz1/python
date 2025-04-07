import subprocess

def is_running(process_name):
    result = subprocess.run(f"pgrep -f {process_name}", shell=True, stdout=subprocess.PIPE)
    return result.returncode == 0

def restart_service(service_name):
    subprocess.run(f"systemctl restart {service_name}", shell=True)

if not is_running("nginx"):
    restart_service("nginx")
    print("nginx was not running and has been restarted.")
else:
    print("nginx is running.")
