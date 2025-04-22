
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("request_logs.json")


def log_request(request_data: dict, response_data: dict):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "request": request_data,
        "response": response_data,
    }

    if LOG_FILE.exists():
        with open(LOG_FILE, "r+") as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
            logs.append(entry)
            f.seek(0)
            json.dump(logs, f, indent=2)
    else:
        with open(LOG_FILE, "w") as f:
            json.dump([entry], f, indent=2)