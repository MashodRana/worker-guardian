import logging
from config import WORKERS
from celery_monitor import is_worker_stuck
from docker_utils import restart_worker_docker
from ssh_utils import restart_worker_ssh
from custom_logging import get_logger
from config import get_settings


logger = get_logger(__name__)
settings = get_settings()


def main():
    for worker_name, info in WORKERS.items():
        try:
            stuck = is_worker_stuck(worker_name, info["queue"])
            if stuck:
                msg = f"{worker_name} is stuck. Attempting restart..."
                logger.warning(msg)
                try:
                    if "ssh_host" in info:
                        restart_worker_ssh(
                            info["ssh_host"],
                            info["ssh_user"],
                            info["ssh_key"],
                            info["docker_container"],
                        )
                    elif "docker_container" in info:
                        restart_worker_docker(info["docker_container"])
                    logging.info(f"✅ {worker_name} restarted successfully.")
                except Exception as e:
                    logging.error(f"❌ Failed to restart {worker_name}. Reason: {e}", exc_info=True)
            else:
                logging.info(f"{worker_name} is healthy.")
        except Exception as e:
            logger.error(
                f"❌ Failed to inspect the worker: {worker_name} for the queue: {info['queue']}. Reason: {e}",
                exc_info=True
            )

if __name__ == "__main__":
    main()
