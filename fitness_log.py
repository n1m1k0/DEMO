# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: FitnessLog
import json
from datetime import datetime

def load_default_data():
    return {
        "user": "Олег",
        "workouts": [
            {
                "date": datetime.now().strftime("%Y-%m-%d"),
                "exercises": [
                    {"name": "Приседания", "sets": [{"weight": 80, "reps": 10}, {"weight": 85, "reps": 8}]},
                    {"name": "Жим лежа", "sets": [{"weight": 60, "reps": 12}]}
                ]
            }
        ],
        "settings": {
            "units": "kg",
            "language": "ru"
        }
    }

def save_data(data):
    with open("fitness_log.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    data = load_default_data()
    save_data(data)
    print(f"Инициализация завершена. Данные сохранены в fitness_log.json.")
