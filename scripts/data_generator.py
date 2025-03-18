import json
import random
from datetime import datetime, timedelta

def generate_threat_data(num_samples):
    data = []
    for _ in range(num_samples):
        record = {
            "timestamp": (datetime.now() - timedelta(minutes=random.randint(0,1440))).isoformat(),
            "severity": round(random.uniform(0.1, 0.99), 2),
            "category": random.sample(["sql_injection", "phishing", "ddos"], 1),
            "source_ip": f"10.0.{random.randint(0,255)}.{random.randint(0,255)}"
        }
        data.append(record)
    with open("data/sample_threat.json", "w") as f:
        json.dump(data, f, indent=2)
