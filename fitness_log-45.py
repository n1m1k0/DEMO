# === Stage 45: Добавь восстановление из резервной копии ===
# Project: FitnessLog
import json, sys
from pathlib import Path

BACKUP_FILE = Path(__file__).parent / "fitness_backup.json"

def load_backup():
    if not BACKUP_FILE.exists():
        print("Резервная копия не найдена.")
        return False
    try:
        with open(BACKUP_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"Резервная копия загружена из {BACKUP_FILE.name}.")
        return True
    except Exception as e:
        print(f"Ошибка при загрузке резервной копии: {e}")
        return False

def restore_backup():
    if not load_backup():
        return
    with open("fitness_log.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Данные успешно восстановлены.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "restore":
        restore_backup()
    else:
        print("Используйте: python fitness_log.py restore")
