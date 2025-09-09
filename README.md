# Worker Guardian

`Worker Guardian` is a Python-based monitoring tool designed to ensure your Celery workers remain healthy and responsive. It automatically detects stuck or idle workers while tasks are pending in the queue and restarts them via Docker or SSH.
This tool is designed to be run periodically via a cron job on Ubuntu systems. It logs all actions to a file for easy tracking and debugging.

---
## Features

- Monitor multiple Celery workers across VMs.
- Detect workers that are idle but have pending tasks in the queue.
- Restart workers automatically via Docker or SSH.
- Log all events and actions to a file with timestamps.
- Simple cron-based deployment, no need for FastAPI or background services.

### 🕒 Set Up Cron Job (Runs Every Hour)

To monitor your workers every hour using a cron job, follow these steps:

---

#### ✅ 1. Make the Script Executable

```bash
chmod +x /path/to/worker-guardian/monitor_workers.py
```

---

#### ✏️ 2. Open Crontab

```bash
crontab -e
```

---

#### 📅 3. Add the Cron Job

Add the following line to the end of the crontab file:

```cron
0 * * * * /usr/bin/python3 /path/to/worker-guardian/monitor_workers.py >> /path/to/worker-guardian/logs/worker_guardian.log 2>&1
```

---

This will:

* Run the script **at the start of every hour** (e.g., 00:00, 01:00, 02:00, ...).
* Append both standard output and error to the log file:

  * `logs/worker_guardian.log`
