# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: FitnessLog
def search_workouts(query, exercises=None, min_sets=1, min_weight=0):
    query = query.lower().strip()
    if not query:
        return [w for w in workouts]
    
    def match(text):
        return text and (text.lower().startswith(query) or query in text.lower())

    results = []
    for workout in workouts:
        sets_data = workout.get('sets', [])
        if exercises and not any(match(e['name']) for e in exercises):
            continue
        if len(sets_data) < min_sets:
            continue
        has_weight = any(s.get('weight') >= min_weight for s in sets_data)
        if not has_weight:
            continue
        
        def contains_query(text):
            return text and query.lower() in text.lower()

        if (contains_query(workout['name']) or 
            contains_query(workout.get('date', '')) or 
            any(contains_query(s.get('notes', '')) for s in sets_data)):
            results.append(workout)
    
    return results
