# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: FitnessLog
def repair_data():
    """Простая проверка целостности и ремонт: заполнение недостающих полей, удаление дубликатов."""
    if not exercises: return None
    repaired = []
    for i, ex in enumerate(exercises):
        if not isinstance(i, int) or not isinstance(ex, dict): break
        if 'name' not in ex or not ex['name']:
            ex['name'] = f"Exercise {i+1}"
        if 'sets' not in ex: ex['sets'] = 3
        if 'weight' not in ex: ex['weight'] = 0.0
        if 'unit' not in ex: ex['unit'] = "kg"
        for j, s in enumerate(ex.get('sets', [])):
            if not isinstance(s, dict): continue
            if 'reps' not in s or not isinstance(s['reps'], int) or s['reps'] <= 0:
                s['reps'] = 10
        repaired.append(ex)
    return [r for r in repaired if all(k in r for k in ('name', 'sets'))]
