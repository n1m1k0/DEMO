# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: FitnessLog
def suggest_next_action(log, exercises):
    if not log:
        return "Начни с базовых упражнений (приседания, отжимания)."
    
    recent = [e for e in log if e['date'] == max(d['date'] for d in log)]
    if not recent:
        most_recent = max(log, key=lambda x: x['date'])
        recent = [most_recent]
    
    total_exercises_done = set()
    for r in recent:
        total_exercises_done.update(r.get('exercises', []))
    
    available = sorted(exercises, key=lambda e: e['difficulty'], reverse=True)
    new_suggestions = [e for e in available if e not in total_exercises_done]
    
    if new_suggestions:
        return f"Попробуй что-то новое: {', '.join(e['name'] for e in new_suggestions[:3])}."
    elif recent and all(r.get('exercises') for r in recent):
        avg_sets = sum(len(r.get('exercises', [])) for r in recent) / len(recent) if recent else 0
        if avg_sets >= 4:
            return "Вы выполняете достаточно подходов! Попробуй увеличить вес или количество повторений."
    
    return "Продолжай регулярно тренироваться и отслеживай прогресс."
