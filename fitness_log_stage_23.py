# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: FitnessLog
def print_training_table(log):
    """Выводит журнал тренировок в формате таблицы консоли."""
    if not log:
        print("Нет данных для отображения.")
        return
    
    # Определяем максимальные ширины столбцов
    max_exercise = max(len(entry['exercise']) for entry in log)
    max_sets = max(len(str(s)) for s in [entry.get('sets', []) for entry in log]) if log else 5
    max_weight = max(max((len(str(w)) for w in sets), default=0) for sets in [entry.get('sets', [[]]) for entry in log]) if log else 3
    max_date = max(len(entry['date']) for entry in log)
    
    # Заголовок таблицы
    header = f"{'Дата':<{max_date}} | {'Упражнение':<{max_exercise}} | {'Подходы':<{max_sets}} | {'Вес (кг)':<{max_weight}}"
    print(header)
    print("-" * len(header))
    
    for entry in log:
        date_str = entry['date'][:10] if isinstance(entry['date'], str) else str(entry['date'])
        exercise_str = entry['exercise']
        sets_data = entry.get('sets', [])
        
        # Формируем строку для подходов и весов
        sets_parts = []
        for i, s in enumerate(sets_data):
            if isinstance(s, dict):
                weight_val = str(s.get('weight', ''))
                reps_str = str(s.get('reps', ''))
                sets_parts.append(f"{reps_str}x{weight_val}")
            else:
                sets_parts.append(str(s))
        
        sets_str = ' | '.join(sets_parts) if sets_parts else 'Нет'
        weight_str = f"{sum(int(s.get('weight', 0)) for s in sets_data) if sets_data else 0:.1f}"
        
        row = f"{date_str:<{max_date}} | {exercise_str:<{max_exercise}} | {sets_str} | {weight_str}"
        print(row)

print_training_table(fitness_log)
