# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: FitnessLog
def demo():
    print("=== FitnessLog Demo ===")
    exercises = [
        {"name": "Приседания", "sets": 3, "weights": [80, 90, 100], "reps": [15, 12, 10]},
        {"name": "Жим лежа", "sets": 4, "weights": [60, 70, 75, 80], "reps": [10, 9, 8, 7]},
        {"name": "Подтягивания", "sets": 3, "weights": [], "reps": [12, 14, 16]},
    ]
    for ex in exercises:
        print(f"\n{ex['name']}:")
        if ex["weights"]:
            weights_str = ", ".join(str(w) + "кг" for w in ex["weights"])
            reps_str = ", ".join(str(r) for r in ex["reps"])
            print(f"  Подходы: {ex['sets']} | Веса: {weights_str} | Повторы: {reps_str}")
        else:
            print(f"  Подходы: {ex['sets']} | Повторы: {', '.join(str(r) for r in ex['reps'])}")

    progress = [
        {"date": "2024-01-15", "total_sets": 3, "avg_weight_kg": 90.0},
        {"date": "2024-01-22", "total_sets": 7, "avg_weight_kg": 72.0},
        {"date": "2024-01-29", "total_sets": 6, "avg_weight_kg": 83.0},
    ]
    print("\n=== Прогресс ===")
    for p in progress:
        print(f"  {p['date']}: {p['total_sets']} подход(ов), средний вес {p['avg_weight_kg']} кг")

    print("\nДемо завершено!")
