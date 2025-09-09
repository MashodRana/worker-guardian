# app/docker_utils.py
import subprocess

from custom_logging import get_logger

logger = get_logger(__name__)


def restart_worker_docker(container_name: str):
    try:
        subprocess.run(["docker", "restart", container_name], check=True)
        logger.info(f"🐳✅ [Docker] Worker {container_name} restarted successfully")
    except subprocess.CalledProcessError as e:
        logger.info(f"🐳❌ [Docker] Failed to restart {container_name}: {e}", exc_info=True)
