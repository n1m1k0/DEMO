# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: FitnessLog
def edit_set(set_id, new_data):
    """Редактирует набор упражнений по ID. Возвращает обновлённый список или None."""
    if not isinstance(new_data, dict) or 'exercise' not in new_data or 'sets' not in new_data:
        return None
    
    edited_sets = []
    for set_item in sets:
        if set_item['id'] == set_id:
            # Обновляем только предоставленные поля, сохраняя остальные (например, дату)
            updated_set = {**set_item, **new_data}
            edited_sets.append(updated_set)
        else:
            edited_sets.append(set_item)
    
    if len(edited_sets) != len(sets):
        return None
    
    sets.clear()
    sets.extend(edited_sets)
    return sets
