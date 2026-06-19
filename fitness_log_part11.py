# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: FitnessLog
import json, os

def save_to_file(data: dict) -> None:
    """Сохраняет данные тренировки в JSON файл."""
    filename = "fitness_log.json"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Данные сохранены в {filename}")
    except IOError as e:
        print(f"[ERROR] Не удалось сохранить файл: {e}")

def load_from_file() -> dict | None:
    """Загружает данные из JSON файла или возвращает пустой словарь."""
    filename = "fitness_log.json"
    if not os.path.exists(filename):
        return {"exercises": [], "history": []}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстанавливаем структуру, если файл был создан в ранней версии без history
        if "history" not in data:
            data["history"] = []
        return data
    except (json.JSONDecodeError, IOError):
        print("[WARN] Файл повреждён или недоступен. Создаётся новый.")
        return {"exercises": [], "history": []}

# Инициализация данных при старте приложения
if __name__ == "__main__":
    db = load_from_file()
    # Пример добавления записи (для демонстрации работы с данными)
    new_set = {
        "exercise": "Приседания",
        "weight": 80,
        "reps": 12,
        "date": "2023-10-27"
    }
    db["history"].append(new_set)
    save_to_file(db)
