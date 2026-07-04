# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: FitnessLog
import json, datetime, os

def save_reminders():
    if not os.path.exists("reminders.json"):
        return
    with open("reminders.json", "r") as f:
        data = json.load(f)
    for uid in list(data.keys()):
        entry = data[uid]
        due_date_str = entry.get("due_date")
        if not due_date_str:
            del data[uid]
            continue
        try:
            due_date = datetime.datetime.fromisoformat(due_date_str)
            now = datetime.datetime.now()
            diff_days = (now - due_date).days
            if diff_days == 0 and entry.get("notified", False):
                pass
            elif diff_days < 0 and not entry.get("completed"):
                print(f"Напоминание: {entry['exercise']} ({due_date_str})")
                entry["notified"] = True
                save_reminders()
        except Exception:
            del data[uid]

def add_due_date(exercise_id, due_date):
    if not os.path.exists("reminders.json"):
        with open("reminders.json", "w") as f:
            json.dump({}, f)
    try:
        with open("reminders.json", "r") as f:
            data = json.load(f)
    except Exception:
        data = {}
    if exercise_id not in data:
        data[exercise_id] = {"due_date": due_date, "notified": False}
    else:
        data[exercise_id]["due_date"] = due_date
    with open("reminders.json", "w") as f:
        json.dump(data, f)

def check_reminders():
    save_reminders()
