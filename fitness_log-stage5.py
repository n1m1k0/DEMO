# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: FitnessLog
def delete_set(set_id: int) -> bool:
    """Удалить запись о подходе по ID. Возвращает True, если удалено, False если не найдено."""
    if set_id not in sets_db:
        print(f"Запись с ID {set_id} не найдена.")
        return False
    
    del sets_db[set_id]
    print(f"Запись с ID {set_id} успешно удалена.")
    return True

def delete_workout(workout_id: int) -> bool:
    """Удалить всю тренировку (все подходы) по ID. Возвращает True, если удалено, False если не найдено."""
    if workout_id not in workouts_db:
        print(f"Тренировка с ID {workout_id} не найдена.")
        return False
    
    # Удаляем все подходы, связанные с этой тренировкой
    for set_id in list(sets_db.keys()):
        if sets_db[set_id].workout_id == workout_id:
            del sets_db[set_id]
    
    del workouts_db[workout_id]
    print(f"Тренировка с ID {workout_id} и все её подходы успешно удалены.")
    return True

def handle_deletion():
    """Простой интерфейс для демонстрации удаления."""
    while True:
        action = input("\nЧто удалить? (1 - подход, 2 - тренировку, q - выход): ").strip()
        
        if action == 'q':
            break
        
        try:
            record_id = int(input("Введите ID записи: "))
        except ValueError:
            print("Неверный формат ID. Введите число.")
            continue
            
        if action == '1':
            delete_set(record_id)
        elif action == '2':
            delete_workout(record_id)
        else:
            print("Неверный выбор действия.")
