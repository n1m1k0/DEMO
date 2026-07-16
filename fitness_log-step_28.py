# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: FitnessLog
def show_metrics():
    if not exercises or not sets:
        print("Нет данных для анализа.")
        return
    total_sets = len(sets)
    completed_exercises = set(e['name'] for e in exercises if any(s.get('done') for s in e.get('sets', [])))
    completion_rate = (len(completed_exercises) / len(exercises)) * 100 if exercises else 0
    avg_weight_per_set = sum(s['weight'] for s in sets if s.get('weight')) / total_sets if total_sets else 0
    avg_reps = sum(s['reps'] for s in sets if s.get('reps')) / total_sets if total_sets else 0
    print(f"Итого подходов: {total_sets}")
    print(f"Завершённых упражнений: {len(completed_exercises)}/{len(exercises)} ({completion_rate:.1f}%)")
    print(f"Средний вес за подход (кг): {avg_weight_per_set:.2f}")
    print(f"Среднее повторений за подход: {avg_reps:.2f}")

if __name__ == '__main__':
    show_metrics()
