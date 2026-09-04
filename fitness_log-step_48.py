# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: FitnessLog
def _clamp(value, lo, hi):
    return max(lo, min(hi, value))

def _format_number(n, unit="kg"):
    if n == int(n):
        return f"{int(n)} {unit}"
    return f"{n:.1f} {unit}"

def _split_lines(text, max_len=80):
    lines = []
    for word in text.split():
        if len(word) + len(lines[-1]) + 1 <= max_len:
            lines[-1] += " " + word
        else:
            lines.append(word)
    return lines

def print_progress_log(user, exercises, history, top_n=5):
    if not history:
        print("  Нет данных для отображения прогресса.")
        return

    ranked = sorted(history, key=lambda h: h["total_volume"], reverse=True)[:top_n]
    print(f"\n  🏆 Топ-{top_n} упражнений по объёму:")
    for ex in ranked:
        print(f"    • {_format_number(ex['total_volume'])} за {ex['total_sets']} подход(ов)")

def print_leaderboard(users, top_n=5):
    if not users:
        print("  Пока нет пользователей.")
        return

    ranked = sorted(users, key=lambda u: u["total_volume"], reverse=True)[:top_n]
    print(f"\n  🏅 Лидеры по общему объёму:")
    for i, u in enumerate(ranked, 1):
        print(f"    {i}. {_format_number(u['total_volume'])} — {u['name']} ({u['streak']} дней)")

def print_menu():
    print("""
    ┌─────────────────────────────────────┐
    │     🏋️‍♂️  FitnessLog v1.0            │
    │                                     │
    │  1. Добавить упражнение             │
    │  2. Добавить подход                 │
    │  3. Сбросить дневной прогресс        │
    │  4. Показать прогресс               │
    │  5. Лидеры                          │
    │  6. Выход                           │
    └─────────────────────────────────────┘
    """)

def main():
    exercises = {}
    history = {}
    users = {}
    daily = {}

    while True:
        print_menu()
        choice = input("  Выберите действие: ").strip()

        if choice == "1":
            name = input("  Название упражнения: ").strip()
            if not name:
                continue
            exercises[name] = {}
            history[name] = []
            print(f"  ✓ Упражнение '{name}' добавлено.")

        elif choice == "2":
            if not exercises:
                print("  Нет упражнений. Добавьте упражнение (1).")
                continue
            name = input("  Название упражнения: ").strip()
            if name not in exercises:
                print("  Упражнение не найдено. Добавьте упражнение (1).")
                continue
            weight = float(input("  Вес (кг): ").strip())
            reps = int(input("  Подходов: ").strip())
            sets = int(input("  Подходов: ").strip())
            if weight <= 0 or reps <= 0 or sets <= 0:
                print("  Некорректные значения.")
                continue
            volume = weight * reps * sets
            today = daily.get(name, 0)
            exercises[name][sets] = volume
            history[name].append({
                "date": "today",
                "weight": weight,
                "reps": reps,
                "sets": sets,
                "volume": volume,
                "streak": today + 1,
            })
            daily[name] = today + 1
            print(f"  ✓ Записано: {_format_number(volume)} за {sets} подход(ов).")

        elif choice == "3":
            if not daily:
                print("  Нет дневных записей.")
                continue
            for name in daily:
                daily[name] = 0
            print("  ✓ Дневной прогресс сброшен.")

        elif choice == "4":
            print_progress_log(None, None, history, top_n=5)

        elif choice == "5":
            print_leaderboard(None, top_n=5)

        elif choice == "6":
            print("  До свидания! 🏋️‍♂️")
            break

        else:
            print("  Неизвестное действие. Попробуйте снова.")

if __name__ == "__main__":
    main()
