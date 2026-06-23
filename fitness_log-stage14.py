# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: FitnessLog
def generate_summary(log):
    if not log:
        return "Нет данных для сводки."
    
    total_workouts = len(log)
    exercises_done = set()
    sets_total = 0
    
    for workout in log:
        ex_name = workout.get("exercise", {}).get("name")
        if ex_name:
            exercises_done.add(ex_name)
        sets_count = workout.get("sets", [])
        sets_total += len(sets_count)
    
    total_volume = sum(sum(set["weight"] * set["reps"] for set in w.get("sets", [])) 
                       for w in log if w.get("exercise"))
    
    return (f"Сводка записей: {total_workouts} тренировок.\n"
            f"Выполнено упражнений: {len(exercises_done)} ({', '.join(sorted(exercises_done))}).\n"
            f"Всего подходов: {sets_total}.\n"
            f"Общий объем работы (кг*повторений): {total_volume:,}")
