# app/docker_utils.py
import subprocess

def restart_worker_docker(container_name: str):
    try:
        subprocess.run(["docker", "restart", container_name], check=True)
        print(f"[Docker] Worker {container_name} restarted successfully")
    except subprocess.CalledProcessError as e:
        print(f"[Docker] Failed to restart {container_name}: {e}")
