import logging
from config import WORKERS
from celery_monitor import is_worker_stuck
from docker_utils import restart_worker_docker
from ssh_utils import restart_worker_ssh
from custom_logging import get_logger
from config import get_settings


logger = get_logger(__name__)
settings = get_settings()
# --- Main monitor function ---
def main():
    for worker_name, info in WORKERS.items():
        stuck = is_worker_stuck(worker_name, info["queue"])
        if stuck:
            msg = f"{worker_name} is stuck. Attempting restart..."
            print(msg)
            logging.warning(msg)
            continue
            try:
                if "docker_container" in info:
                    restart_worker_docker(info["docker_container"])
                elif "ssh_host" in info:
                    restart_worker_ssh(
                        info["ssh_host"],
                        info["ssh_user"],
                        info["ssh_key"],
                        info["docker_container"],
                    )
                logging.info(f"{worker_name} restarted successfully.")
            except Exception as e:
                logging.error(f"Failed to restart {worker_name}: {e}")
        else:
            logging.info(f"{worker_name} is healthy.")

if __name__ == "__main__":
    main()
