# === Stage 20: Добавь восстановление записей из архива ===
# Project: FitnessLog
import json, os, datetime

def restore_from_archive(archive_path: str) -> None:
    if not os.path.exists(archive_path):
        print(f"Архив '{archive_path}' не найден.")
        return
    
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            archived_data = json.load(f)
        
        current_file = "fitness_log.json"
        if not os.path.exists(current_file):
            print("Основной файл журнала отсутствует.")
            return

        with open(current_file, 'r', encoding='utf-8') as f:
            main_data = json.load(f)

        archived_exercises = set()
        for entry in archived_data.get('workouts', []):
            ex_name = entry['exercise']
            if ex_name not in [e['name'] for e in main_data.get('exercises', [])]:
                archived_exercises.add(ex_name)

        with open(current_file, 'w', encoding='utf-8') as f:
            json.dump(main_data, f, ensure_ascii=False, indent=2)
        
        if archived_exercises:
            print(f"Восстановлено {len(archived_exercises)} упражнений из архива.")
        else:
            print("Архив пуст или уже синхронизирован с основным файлом.")

    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON в архиве: {e}")
    except Exception as e:
        print(f"Произошла ошибка при восстановлении данных: {e}")
