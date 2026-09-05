# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: FitnessLog
def self_check_and_report():
    """Финальная самопроверка: импортируем все классы и проверяем, что приложение готово."""
    from classes import (
        Exercise, ExerciseSet, Workout, WorkoutDay,
        User, App
    )

    # 1. Проверяем базовые объекты
    ex = Exercise("Push-ups", 5)
    assert isinstance(ex, Exercise)
    ex.add_set(ExerciseSet(10, 20, 5))
    assert len(ex.sets) == 1

    # 2. Проверяем день тренировки
    day = WorkoutDay("Monday")
    assert isinstance(day, WorkoutDay)
    day.add_workout(Workout(ex, 1))
    assert len(day.workouts) == 1

    # 3. Проверяем пользователя и приложение
    user = User("Alice", "alice@example.com", "1990-01-01")
    assert isinstance(user, User)
    app = App(user)
    assert isinstance(app, App)

    # 4. Проверяем записи в журнал
    journal = app.get_journal()
    assert isinstance(journal, list)

    # 5. Проверяем статистику
    stats = app.get_stats()
    assert isinstance(stats, dict)

    # 6. Проверяем прогресс
    progress = app.get_progress()
    assert isinstance(progress, dict)

    print("=" * 40)
    print("✅ FitnessLog — финальная самопроверка пройдена!")
    print("=" * 40)
    print("📋 Проверено:")
    print("  • Класс Exercise и добавление подходов")
    print("  • Класс WorkoutDay и добавление тренировок")
    print("  • Класс User и создание приложения")
    print("  • Метод get_journal()")
    print("  • Метод get_stats()")
    print("  • Метод get_progress()")
    print("=" * 40)
    print("🚀 Приложение FitnessLog готово к использованию!")
    print("=" * 40)

    return True

if __name__ == "__main__":
    self_check_and_report()
