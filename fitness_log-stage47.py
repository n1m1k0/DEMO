# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: FitnessLog
def demo():
    print("=== FitnessLog Demo ===")
    user = User("Анна", date.today())
    user.set_goal("Подтягивания", 10, 3)
    print(f"Цель: {user.goal}\n")

    user.log_session("Вечер", [
        ("Подтягивания", 3, 8, 0),
        ("Отжимания", 3, 15, 0),
        ("Приседания", 4, 20, 0),
        ("Планка", 3, 45, 0),
    ])
    print(user.get_last_session_summary())

    user.log_session("Утро", [
        ("Подтягивания", 3, 10, 0),
        ("Отжимания", 3, 20, 0),
        ("Приседания", 4, 25, 0),
        ("Планка", 3, 60, 0),
    ])
    print(user.get_last_session_summary())

    user.log_session("Вечер", [
        ("Подтягивания", 3, 12, 0),
        ("Отжимания", 3, 25, 0),
        ("Приседания", 4, 30, 0),
        ("Планка", 3, 75, 0),
    ])
    print(user.get_last_session_summary())

    print(f"\nПрогресс: {user.get_progress()}")
    print("Демо завершён. Спасибо за использование FitnessLog!")
