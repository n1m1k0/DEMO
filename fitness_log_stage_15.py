# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: FitnessLog
def get_weekly_stats(records, start_date):
    from datetime import timedelta, date
    week_start = start_date - timedelta(days=start_date.weekday())
    week_end = week_start + timedelta(weeks=1)
    weekly_data = {date: {'exercises': 0, 'total_sets': 0, 'total_volume': 0} for date in range(week_start, week_end)}
    for rec in records:
        if start_date <= rec['date'] < week_end:
            weekly_data[rec['date']]['exercises'] += len(rec.get('sets', []))
            weekly_data[rec['date']]['total_sets'] += len(rec.get('sets', []))
            weekly_data[rec['date']]['total_volume'] += sum(set['weight'] * set['reps'] for set in rec.get('sets', []))
    return {k: v for k, v in sorted(weekly_data.items()) if v['exercises'] > 0}
