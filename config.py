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
        "docker_container": "celery_audio_splitter_worker",
        "ssh_host": "worker-vm-ip",       # optional if using SSH
        "ssh_user": "user",
        "ssh_key": "/path/to/key.pem"
    },
    "nlp_worker": {
        "queue": "nlp_task_queue",
        "docker_container": "celery_nlp_worker",
        "ssh_host": "worker-vm-ip",
        "ssh_user": "user",
        "ssh_key": "/path/to/key.pem"
    }
}
