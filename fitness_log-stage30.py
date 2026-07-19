# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: FitnessLog
def switch_profile():
    print("Выберите профиль:")
    for i, p in enumerate(user_profiles):
        print(f"  {i+1}. {p['name']}")
    choice = int(input()) - 1
    if 0 <= choice < len(user_profiles):
        return user_profiles[choice]
    print("Неверный выбор")
    return None

def save_profile(name, exercises=None):
    global current_user
    if exercises is None:
        exercises = []
    current_user = User(name)
    for e in exercises:
        current_user.add_exercise(e)
    user_profiles.append({
        "name": name,
        "exercises": [e.to_dict() for e in exercises]
    })

def list_profiles():
    if not user_profiles:
        print("Нет сохранённых профилей. Создайте один через save_profile().")
        return []
    return user_profiles
