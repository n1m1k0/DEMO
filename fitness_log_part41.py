# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: FitnessLog
# Mode: dry-run for data operations (Exercise, Set, Progress)
# Returns a dict with 'ok' bool and optional error message.
# Used before real DB writes to validate changes without persisting them.

def _dry_run_log(message):
    print(f"[DRY-RUN] {message}")
    return {"ok": True, "error": None}

def dry_run_add_exercise(exercise_data):
    if not exercise_data or isinstance(exercise_data, dict) and not exercise_data.get("name"):
        _dry_run_log("Invalid exercise data: missing 'name'")
        return {"ok": False, "error": "Missing required field: name"}
    _dry_run_log(f"Would insert Exercise(id={exercise_data.get('id', -1)}, name='{exercise_data['name']}')")
    return {"ok": True, "error": None}

def dry_run_add_set(set_data):
    if not set_data or isinstance(set_data, dict) and not all(k in set_data for k in ("exercise_id", "reps", "weight")):
        _dry_run_log("Invalid set data: missing required fields")
        return {"ok": False, "error": "Missing required fields: exercise_id, reps, weight"}
    _dry_run_log(f"Would insert Set(exercise_id={set_data['exercise_id']}, reps={set_data['reps']}, weight={set_data['weight']})")
    return {"ok": True, "error": None}

def dry_run_update_progress(progress_data):
    if not progress_data or isinstance(progress_data, dict) and not all(k in progress_data for k in ("exercise_id", "best_weight", "best_reps")):
        _dry_run_log("Invalid progress data: missing required fields")
        return {"ok": False, "error": "Missing required fields: exercise_id, best_weight, best_reps"}
    _dry_run_log(f"Would update Progress(exercise_id={progress_data['exercise_id']}, best_weight={progress_data['best_weight']}kg, best_reps={progress_data['best_reps']}x)")
    return {"ok": True, "error": None}

# Example usage (uncomment to test):
# print(dry_run_add_exercise({"id": 101, "name": "Bench Press"}))
# print(dry_run_add_set({"exercise_id": 101, "reps": 8, "weight": 65.0}))
# print(dry_run_update_progress({"exercise_id": 101, "best_weight": 72.5, "best_reps": 10}))
