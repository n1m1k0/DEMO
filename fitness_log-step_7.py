# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: FitnessLog
def sort_workouts(workouts, key='date'):
    if key == 'date':
        return sorted(workouts, key=lambda w: w['timestamp'], reverse=True)
    elif key == 'priority':
        return sorted(workouts, key=lambda w: -w.get('priority', 0))
    elif key == 'name':
        return sorted(workouts, key=lambda w: w['exercise_name'].lower())
    else:
        return workouts
