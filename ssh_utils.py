import paramiko

from custom_logging import get_logger


logger = get_logger(__name__)


def restart_worker_ssh(host, user, key_file, container_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, key_filename=key_file)
    ssh.exec_command(f"docker restart {container_name}")
    ssh.close()
    logger.info(f"🔁 [SSH] Worker {container_name} on 🖥️ {host} restarted")
