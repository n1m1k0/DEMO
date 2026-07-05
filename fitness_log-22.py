# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: FitnessLog
def check_overdue_reminders():
    now = datetime.now()
    overdue = []
    for reminder in reminders:
        if reminder['date'] < now and not reminder['sent']:
            overdue.append(reminder)
    return overdue
