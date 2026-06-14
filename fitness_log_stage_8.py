# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: FitnessLog
def main_menu():
    while True:
        print("\n=== FitnessLog ===")
        print("1. Добавить упражнение")
        print("2. Просмотреть историю")
        print("3. Выход")
        choice = input("Выберите действие (1-3): ")
        if choice == "1":
            exercise_name = input("Название упражнения: ").strip() or "Не указано"
            sets_count = int(input("Количество подходов: ")) or 0
            weight_kg = float(input("Вес (кг): ")) or 0.0
            date_str = input("Дата (ДД.ММ.ГГГГ): ") or datetime.now().strftime("%d.%m.%Y")
            workouts.append({
                "exercise": exercise_name,
                "sets": sets_count,
                "weight": weight_kg,
                "date": date_str
            })
            print("Упражнение добавлено!")
        elif choice == "2":
            if not workouts:
                print("История пуста.")
            else:
                for i, workout in enumerate(workouts):
                    print(f"\n{workout['date']} | {workout['exercise']}: {workout['sets']} подходов x {workout['weight']} кг")
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")
