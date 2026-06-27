# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: FitnessLog
def get_monthly_stats(exercises, start_date, end_date):
    from datetime import date
    stats = {}
    for ex in exercises:
        if not hasattr(ex, 'date') or not isinstance(ex.date, date): continue
        d = ex.date
        key = f"{d.year}-{d.month}"
        if key not in stats: stats[key] = {'exercises': [], 'total_sets': 0, 'total_weight': 0}
        if start_date <= d <= end_date:
            stats[key]['exercises'].append(ex.name)
            stats[key]['total_sets'] += len(ex.sets)
            stats[key]['total_weight'] += sum(s.weight for s in ex.sets)
    return stats
