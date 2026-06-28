# === Stage 17: Добавь группировку записей по категориям ===
# Project: FitnessLog
from collections import defaultdict

def group_by_category(records):
    grouped = defaultdict(list)
    for record in records:
        category = record.get('category', 'Other')
        grouped[category].append(record)
    return dict(sorted(grouped.items()))

if __name__ == "__main__":
    sample_records = [
        {"exercise": "Push-ups", "sets": 3, "weight": None, "date": "2024-10-01"},
        {"exercise": "Squats", "sets": 4, "weight": 80, "date": "2024-10-01"},
        {"exercise": "Push-ups", "sets": 5, "weight": None, "date": "2024-10-03"}
    ]
    
    # Добавляем категорию для каждого упражнения (упрощенно: первая буква названия)
    for r in sample_records:
        cat = ''.join(word[0] for word in r['exercise'].split())
        r['category'] = cat
    
    grouped_data = group_by_category(sample_records)
    
    print("Группировка по категориям:")
    for category, items in grouped_data.items():
        print(f"\n{category}:")
        for item in items:
            print(f"  - {item['exercise']}: {item['sets']} подходов")
