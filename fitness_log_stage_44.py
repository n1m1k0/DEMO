# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: FitnessLog
import os
from datetime import datetime

def backup_data_file(data_file_path, backup_dir="backups"):
    if not os.path.exists(data_file_path):
        print(f"Файл данных не найден: {data_file_path}")
        return None
    os.makedirs(backup_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"data_backup_{ts}.json")
    with open(data_file_path, "r", encoding="utf-8") as src:
        data = src.read()
    with open(backup_path, "w", encoding="utf-8") as dst:
        dst.write(data)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path
