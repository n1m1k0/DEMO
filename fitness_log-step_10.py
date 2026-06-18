# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: FitnessLog
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.now().isoformat(),
        "exercises": exercises,
        "stats": stats if 'stats' in globals() else {},
        "settings": settings if 'settings' in globals() else {}
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
