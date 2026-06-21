# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: FitnessLog
import json, os

def load_from_file(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден.")
            return {}
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and ('exercises' in data or 'workouts' in data):
                print("Данные успешно загружены из JSON.")
                return data
            else:
                raise ValueError("Неверный формат данных в файле.")
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON файла: {e}")
    except IOError as e:
        print(f"Ошибка доступа к файлу: {e}")
    return {}

# Пример вызова (раскомментируй для использования)
# data = load_from_file('fitness_data.json')
