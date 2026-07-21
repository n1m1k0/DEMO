# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: FitnessLog
def switch_profile():
    if not profiles:
        print("Нет доступных профилей. Добавьте профиль через add_profile().")
        return
    for i, p in enumerate(profiles):
        print(f"[{i}] {p['name']} (ID: {p['id']})")
    try:
        choice = int(input("\nВыберите индекс профиля или 0 для текущего: "))
    except ValueError:
        print("Введите число.")
        return
    if choice == 0:
        set_active_profile(current_user_id)
        return
    idx = (choice % len(profiles)) + 1
    if profiles[idx - 2] and profiles[idx - 2]['id'] != current_user_id:
        new_id = profiles[idx - 2]['id']
        set_active_profile(new_id)
