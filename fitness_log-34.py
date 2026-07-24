# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: FitnessLog
TEMPLATES = {
    "push": {"name": "Push Day", "exercises": [
        {"name": "Push-ups", "sets": 3, "reps": 15},
        {"name": "Dumbbell Press", "sets": 4, "weight": 20, "reps": 10},
    ]},
    "pull": {"name": "Pull Day", "exercises": [
        {"name": "Pull-ups", "sets": 3, "reps": 8},
        {"name": "Bicep Curls", "sets": 3, "weight": 15, "reps": 12},
    ]},
    "legs": {"name": "Legs Day", "exercises": [
        {"name": "Squats", "sets": 4, "weight": 60, "reps": 8},
        {"name": "Lunges", "sets": 3, "weight": 25, "reps": 12},
    ]},
}

def apply_template(template_name):
    if template_name not in TEMPLATES:
        print(f"Unknown template: {template_name}")
        return None
    t = TEMPLATES[template_name]
    entry = {"date": datetime.now().strftime("%Y-%m-%d"), "exercises": []}
    for ex in t["exercises"]:
        if "weight" in ex and "reps" in ex:
            entry["exercises"].append({"name": ex["name"], "sets": ex["sets"], "weight": ex["weight"], "reps": ex["reps"]})
        else:
            entry["exercises"].append({"name": ex["name"], "sets": ex["sets"], "reps": ex["reps"]})
    return entry

def get_templates():
    return TEMPLATES
