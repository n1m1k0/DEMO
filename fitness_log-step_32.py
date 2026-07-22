# === Stage 32: Добавь журнал действий пользователя ===
# Project: FitnessLog
import json, os

class ActionLog:
    def __init__(self):
        self.actions = []
        self._load()
    
    def _load(self):
        path = 'actions.json'
        if not os.path.exists(path):
            return
        with open(path) as f:
            data = json.load(f)
        self.actions = [Action(**a) for a in data]
    
    def save(self):
        path = 'actions.json'
        data = [{'type': a.type, **a.__dict__} for a in self.actions]
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)

class Action:
    def __init__(self, type, date=None, note='', weight=None):
        import datetime
        if not date:
            date = str(datetime.date.today())
        self.type = type  # 'exercise', 'rest', 'water_break'
        self.date = date
        self.note = note
        self.weight = weight

    def to_dict(self):
        return {'type': self.type, 'date': self.date, 'note': self.note, 'weight': self.weight}
