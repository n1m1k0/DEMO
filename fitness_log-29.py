# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: FitnessLog
def get_app_settings():
    return {
        "app_name": "FitnessLog",
        "version": "0.29",
        "default_exercises": [
            {"name": "Push-ups", "target_sets": 3, "target_reps": 15},
            {"name": "Squats", "target_sets": 4, "target_reps": 20},
            {"name": "Pull-ups", "target_sets": 3, "target_reps": 8},
        ],
        "date_format": "%Y-%m-%d",
        "log_file_path": "./fitness_log.txt",
    }

APP_SETTINGS = get_app_settings()


def load_from_config(exercises_list=None):
    if exercises_list is None:
        return [get_exercise(name, s["target_sets"], s["target_reps"]) for s in APP_SETTINGS["default_exercises"]]
    return exercises_list


def log_with_format(entry, fmt=APP_SETTINGS["date_format"]):
    return entry.strftime(fmt)
