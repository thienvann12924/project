import time
import random
import requests
from datetime import datetime, timedelta

API_KEY = "7a1a1972-3985-44fe-a078-0f19eb1ed764"
API_URL = "https://hackatime.hackclub.com/api/hackatime/v1/users/current/heartbeats"

fake_files = [
    "app/main.py", "utils/helpers.py", "tests/test_api.py",
    "models/user.py", "routes/auth.py", "README.md"
]
branches = ["main", "dev", "feature/login", "hotfix/typo"]
project_name = "internal-colab-sim"

def send_heartbeat(file, language, is_write=False, is_save=False):
    payload = [{
        "type": "file",
        "time": time.time(),
        "entity": file,
        "language": language,
        "is_write": is_write,
        "is_save": is_save,
        "project": project_name,
        "branch": random.choice(branches),
        "cursorpos": random.randint(1, 5000),
        "lineno": random.randint(1, 200),
        "plugin": "vscode/1.89.0",
        "editor": "Visual Studio Code",
        "platform": "Windows",
        "category": "coding"
    }]
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    res = requests.post(API_URL, headers=headers, json=payload)
    status = res.status_code
    print(f"[{datetime.now().isoformat()}] ➜ {file}, write={is_write}, save={is_save}, status={status}")
    if status >= 400:
        print("  ↪ Response:", res.text)

def simulate_workday(hours=8):
    end_time = datetime.now() + timedelta(hours=hours)
    current_file = random.choice(fake_files)

    while datetime.now() < end_time:
        if random.random() < 0.1:
            current_file = random.choice(fake_files)
            print(f"📁 Switched to: {current_file}")

        is_write = random.random() < 0.8
        is_save = random.random() < 0.2
        language = "Python" if current_file.endswith(".py") else "Markdown"

        send_heartbeat(current_file, language, is_write, is_save)
        time.sleep(random.uniform(30, 180))

if __name__ == "__main__":
    simulate_workday()
