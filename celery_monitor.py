# app/celery_monitor.py
from celery import Celery
from celery.exceptions import TimeoutError
import redis
# from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD
from config import get_settings
from custom_logging import get_logger


logger = get_logger(__name__)
settings = get_settings()

celery_app = Celery("worker_guardian", broker=settings.broker_url, backend=settings.result_backend_url)
# print(REDIS_HOST, REDIS_PASSWORD)
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.BROKER_DB_NUMBER, password=settings.REDIS_PASSWORD)

def is_worker_stuck(worker_name: str, queue_name: str) -> bool:
    try:
        logger.info(f"🔍 Inspecting the worker: {worker_name} for queue: {queue_name}...")
        inspector = celery_app.control.inspect(timeout=20)
        active = inspector.active() or {}
        reserved = inspector.reserved() or {}

        active_tasks = active.get(f"celery@{worker_name}", [])
        reserved_tasks = reserved.get(f"celery@{worker_name}", [])

        pending_tasks = r.llen(queue_name)

        return len(active_tasks) == 0 and len(reserved_tasks) == 0 and pending_tasks > 0
    except TimeoutError:
        return True  # consider worker stuck if inspect fails
