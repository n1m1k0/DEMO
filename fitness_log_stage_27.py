# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: FitnessLog
def _generate_demo_data():
    """Создает демо-данные для демонстрации приложения."""
    return {
        "exercises": [
            {"id": 1, "name": "Приседания", "muscle_group": "Ноги"},
            {"id": 2, "name": "Отжимания", "muscle_group": "Грудь"},
            {"id": 3, "name": "Подтягивания", "muscle_group": "Спина"},
            {"id": 4, "name": "Планка", "muscle_group": "Кор"},
        ],
        "workouts": [
            {
                "date": "2024-01-15",
                "exercise_id": 1,
                "sets": [{"rep": 10, "weight_kg": 60}, {"rep": 12, "weight_kg": 60}],
            },
            {
                "date": "2024-01-15",
                "exercise_id": 3,
                "sets": [{"rep": 8, "weight_kg": 75}, {"rep": 9, "weight_kg": 75}],
            },
        ],
    }


def clear_all_data():
    """Полностью очищает все данные приложения."""
    global exercises, workouts

    # Очищаем текущие данные в памяти
    if isinstance(exercises, list):
        exercises.clear()
    elif hasattr(exercises, 'clear'):
        exercises.clear()

    if isinstance(workouts, list):
        workouts.clear()
    elif hasattr(workouts, 'clear'):
        workouts.clear()


# Инициализация демо-данных при запуске
exercises = _generate_demo_data()["exercises"]
workouts = _generate_demo_data()["workouts"]
