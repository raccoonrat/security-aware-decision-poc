import json
from datetime import datetime

class ThreatLoader:
    def __init__(self, file_path):
        with open(file_path) as f:
            raw_data = json.load(f)
        self.data = [self._parse_record(r) for r in raw_data]

    def _parse_record(self, record):
        return {
            **record,
            "timestamp": datetime.fromisoformat(record["timestamp"])
        }
