import json
from datetime import datetime


def log_step(step, data):

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "step": step,
        "data": data
    }

    print(json.dumps(log_entry, indent=2))