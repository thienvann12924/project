
from datetime import datetime, timedelta
import time
import requests
import random
import os
# import threading
# from http.server import HTTPServer, BaseHTTPRequestHandler


# class DummyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b"Service is alive.")

# def start_dummy_server():
#     server = HTTPServer(("0.0.0.0", 10000), DummyHandler)
#     server.serve_forever()

# threading.Thread(target=start_dummy_server, daemon=True).start()


# 🛡️ Thay bằng API KEY HackaTime thật của bạn (lấy từ lệnh setup.ps1)
API_KEY = "7a1a1972-3985-44fe-a078-0f19eb1ed764"
API_URL = "https://hackatime.hackclub.com/api/hackatime/v1/users/current/heartbeats"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


# ⏱️ Project và thời gian giả lập (phút)
project_blocks = [
    ("analytics_engine", 5 * 60 + 14),
    ("project-2", 2 * 60 + 8),
    ("project-3", 60 + 8),
    ("analytics_platform", 27),
    ("Petshop-master", 14),
    ("card", 10),
    ("calculator-app", 7),
]

# 🗂️ File giả lập cho từng project
project_files = {
    "analytics_engine": ["data/processor.py", "api/main.py", "models/model.py"],
    "project-2": ["main.py", "utils/helper.py", "views/page.html"],
    "project-3": ["src/app.js", "components/button.jsx"],
    "analytics_platform": ["etl/run_pipeline.py", "etl/config.yaml"],
    "Petshop-master": ["store/cart.py", "store/checkout.py"],
    "card": ["card/generator.py"],
    "calculator-app": ["calc/engine.py", "calc/ui.py"],
}

def send_heartbeat(project, filename, timestamp, is_write=False, is_save=False):
    payload = {
        "entity": filename,
        "time": timestamp,
        "type": "file",
        "project": project,
        "language": "Python",
        "is_write": is_write,
        "is_save": is_save,
        "branch": "main",
        "cursorpos": {
            "row": random.randint(1, 120),
            "column": random.randint(1, 80)
        },
        "plugin": "Windows/Vscode",
        "category": "coding"
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    print(f"[{datetime.utcnow()}] ✅ Heartbeat ➜ Project: {project}, File: {filename}, Write: {is_write}, Save: {is_save}, Status: {response.status_code}")
    return response.status_code


# ▶️ Chạy mô phỏng
start_time = datetime.utcnow()
current_time = start_time

for project, duration_minutes in project_blocks:
    end_time = current_time + timedelta(minutes=duration_minutes)
    files = project_files.get(project, ["main.py"])

    while current_time < end_time:
        filename = random.choice(files)
        timestamp = current_time.timestamp()
        is_write = random.random() < 0.6
        is_save = random.random() < 0.4

        send_heartbeat(project, filename, timestamp, is_write, is_save)

        # Gửi mỗi 30–60 giây (có thể giảm time.sleep khi test)
        interval = random.randint(30, 60)
        current_time += timedelta(seconds=interval)
        time.sleep(2)  # ⚠️ Khi chạy thật hãy dùng: time.sleep(interval)

print("🎉 Simulation complete.")

