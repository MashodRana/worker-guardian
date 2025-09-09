from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""
    BROKER_DB_NUMBER: int = 0
    RESULT_BACKEND_DB_NUMBER: int = 1

    @property
    def broker_url(self):
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.BROKER_DB_NUMBER}"

    @property
    def result_backend_url(self):
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.RESULT_BACKEND_DB_NUMBER}"

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "ignore"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings():
    return Settings()


# Workers config
WORKERS = {
    "audio_splitter_worker": {
        "queue": "audio_splitter_task_queue",
        "docker_container": "audio-splitter-worker",
        # "ssh_host": "57.155.90.3",       # optional if using SSH
        # "ssh_user": "azureuser",
        # "ssh_key": r"D:\vivasoft\stickler\pem_keys\stickler-dev-trie-service-vm_key.pem"
    },
    "transcriptor_worker": {
        "queue": "transcription_task_queue",
        "docker_container": "transcriptor-worker",
        "ssh_host": "20.191.147.182",
        "ssh_user": "azureuser",
        "ssh_key": r"D:\vivasoft\stickler\pem_keys\stickler-dev-transcription-service-vm_key.pem"
    },
    "completion_notifier_worker": {
        "queue": "process_completion_task_queue",
        "docker_container": "completion-notifier-worker",
        # "ssh_host": "57.155.90.3",       # optional if using SSH
        # "ssh_user": "azureuser",
        # "ssh_key": r"D:\vivasoft\stickler\pem_keys\stickler-dev-trie-service-vm_key.pem"
    },
}
