# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: FitnessLog
def filter_workouts(workouts, filters=None):
    if not filters: return workouts
    status = filters.get('status')
    category = filters.get('category')
    tags = filters.get('tags', [])
    result = []
    for w in workouts:
        if status and w['status'] != status: continue
        if category and w.get('category') != category: continue
        if tags and not any(t in w.get('tags', []) for t in tags): continue
        result.append(w)
    return result
