# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: FitnessLog
DATA_VERSION = 2

def migrate_v1_to_v2(data):
    """Миграция v1 -> v2: добавляем поле is_completed к каждому сету."""
    if not isinstance(data, dict):
        return data
    if data.get("version") != 1:
        return data
    for exercise in data.get("exercises", []):
        for set_entry in exercise.get("sets", []):
            set_entry["is_completed"] = set_entry.get("completed", False)
    data["version"] = 2
    return data
