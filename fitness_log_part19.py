# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: FitnessLog
def archive_old_records(cutoff_date, output_file='archive.json'):
    from datetime import datetime, timedelta
    import json
    
    today = datetime.now()
    cutoff = cutoff_date or (today - timedelta(days=365))
    
    archived = []
    remaining = []
    
    with open('data.json', 'r') as f:
        records = json.load(f)
    
    for record in records['workouts']:
        if datetime.strptime(record['date'], '%Y-%m-%d') < cutoff:
            archived.append(record)
        else:
            remaining.append(record)
    
    with open('data.json', 'w') as f:
        json.dump({'workouts': remaining}, f, ensure_ascii=False, indent=2)
    
    if archived:
        with open(output_file, 'w') as f:
            json.dump({'archived_workouts': archived}, f, ensure_ascii=False, indent=2)
        print(f"Архивировано {len(archived)} записей в '{output_file}'")
