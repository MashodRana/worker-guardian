# Worker Guardian

`Worker Guardian` is a Python-based monitoring tool designed to ensure your Celery workers remain healthy and responsive. It automatically detects stuck or idle workers while tasks are pending in the queue and restarts them via Docker or SSH.
This tool is designed to be run periodically via a cron job on Ubuntu systems. It logs all actions to a file for easy tracking and debugging.

## Features

- Monitor multiple Celery workers across VMs.
- Detect workers that are idle but have pending tasks in the queue.
- Restart workers automatically via Docker or SSH.
- Log all events and actions to a file with timestamps.
- Simple cron-based deployment, no need for FastAPI or background services.
