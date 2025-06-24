# import time
# import random
# import requests
# from datetime import datetime, timedelta

# API_KEY = "7a1a1972-3985-44fe-a078-0f19eb1ed764"
# API_URL = "https://hackatime.hackclub.com/api/hackatime/v1/users/current/heartbeats"

# fake_files = [
#     "app/main.py", "utils/helpers.py", "tests/test_api.py",
#     "models/user.py", "routes/auth.py", "README.md"
# ]
# branches = ["main", "dev", "feature/login", "hotfix/typo"]
# project_name = "internal-colab-sim"

# def send_heartbeat(file, language, is_write=False, is_save=False):
#     payload = [{
#         "type": "file",
#         "time": time.time(),
#         "entity": file,
#         "language": language,
#         "is_write": is_write,
#         "is_save": is_save,
#         "project": project_name,
#         "branch": random.choice(branches),
#         "cursorpos": random.randint(1, 5000),
#         "lineno": random.randint(1, 200),
#         "plugin": "vscode/1.89.0",
#         "editor": "Visual Studio Code",
#         "platform": "Windows",
#         "category": "coding"
#     }]
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
#     res = requests.post(API_URL, headers=headers, json=payload)
#     status = res.status_code
#     print(f"[{datetime.now().isoformat()}] ➜ {file}, write={is_write}, save={is_save}, status={status}")
#     if status >= 400:
#         print("  ↪ Response:", res.text)

# def simulate_workday(hours=8):
#     end_time = datetime.now() + timedelta(hours=hours)
#     current_file = random.choice(fake_files)

#     while datetime.now() < end_time:
#         if random.random() < 0.1:
#             current_file = random.choice(fake_files)
#             print(f"📁 Switched to: {current_file}")

#         is_write = random.random() < 0.8
#         is_save = random.random() < 0.2
#         language = "Python" if current_file.endswith(".py") else "Markdown"

#         send_heartbeat(current_file, language, is_write, is_save)
#         time.sleep(random.uniform(30, 180))

# if __name__ == "__main__":
#     simulate_workday()



from datetime import datetime, timedelta
import time
import requests
import random
import os

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
        "plugin": "Windows/Visual Studio Code",
        "category": "coding"
        # "editor": "Visual Studio Code",
        # "operating_system": "Windows",
        # "plugin": "vscode/1.89.0",  # 🆕 Quan trọng!
        # "category": "coding"
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    print(f"[{datetime.utcnow()}] ✅ Heartbeat ➜ Project: {project}, File: {filename}, Write: {is_write}, Save: {is_save}, Status: {response.status_code}")
    return response.status_code

#Ver 3.0
# def send_heartbeat(project, filename, timestamp, is_write=False, is_save=False):
#     payload = {
#         "entity": filename,
#         "time": timestamp,
#         "type": "file",
#         "project": project,
#         "language": "Python",
#         "is_write": is_write,
#         "is_save": is_save,
#         "branch": "main",
#         "cursorpos": {
#             "row": random.randint(1, 120),
#             "column": random.randint(1, 80)
#         },
#         "editor": "Visual Studio Code",
#         "operating_system": "Windows"
#     }

#     # 👇 Gửi đúng định dạng object, không phải array
#     response = requests.post(API_URL, headers=HEADERS, json=payload)

#     print(f"[{datetime.utcnow()}] ✅ Heartbeat ➜ Project: {project}, File: {filename}, Write: {is_write}, Save: {is_save}, Status: {response.status_code}")
#     return response.status_code


# Ver 2.0
# def send_heartbeat(project, filename, timestamp, is_write=False, is_save=False):
#     payload = {
#         "entity": filename,
#         "time": timestamp,
#         "type": "file",
#         "project": project,
#         "language": "Python",
#         "is_write": is_write,
#         "is_save": is_save,
#         "branch": "main",
#         "cursorpos": {"row": random.randint(1, 120), "column": random.randint(1, 80)},
#         "editor": "Visual Studio Code",
#         "operating_system": "Windows"
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=[payload])
#     status = response.status_code
#     print(f"[{datetime.utcnow()}] ✅ Heartbeat ➜ Project: {project}, File: {filename}, Write: {is_write}, Save: {is_save}, Status: {status}")
#     return status

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
        time.sleep(0.1)  # ⚠️ Khi chạy thật hãy dùng: time.sleep(interval)

print("🎉 Simulation complete.")

