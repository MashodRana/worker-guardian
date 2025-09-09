import logging
from functools import lru_cache
from pathlib import Path


# --- Logging setup ---
LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "worker_guardian.log"


@lru_cache(maxsize=1)
def _configure_logging():
    """Configure logging once for the whole app."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return True

def get_logger(name: str):
    """
    Return a logger for the given module name.
    Example: logger = get_logger(__name__)
    """
    _configure_logging()
    return logging.getLogger(name)
