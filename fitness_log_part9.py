# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: FitnessLog
import json, sys

INITIAL_DATA = '''
{
    "exercises": [
        {"id": 1, "name": "Приседания", "muscle_group": "Ноги"},
        {"id": 2, "name": "Жим лежа", "muscle_group": "Грудь"}
    ],
    "workouts": []
}
'''

def load_initial_data():
    try:
        return json.loads(INITIAL_DATA)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга начальных данных: {e}", file=sys.stderr)
        sys.exit(1)

initial_db = load_initial_data()
