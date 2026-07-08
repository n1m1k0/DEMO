# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: FitnessLog
def print_set_summary(set_):
    """One-line summary of a single set."""
    return (f"[{set_['id']}] {set_['exercise']['name']:15} "
            f"x={set_['reps']:>2}  w={set_['weight_kg']:>4.0f}kg  "
            f"note={set_.get('note', '')}")

def print_workout_summary(workout):
    """Compact one-paragraph summary of the whole workout."""
    sets = workout.get("sets", [])
    total_reps = sum(s["reps"] for s in sets)
    total_weight = sum(s["weight_kg"] * s["reps"] for s in sets)
    lines = [f"Workout #{workout['id']} | {len(sets)} sets | {total_reps} reps | "
             f"{total_weight:.0f} kg · {':'.join(workout.get('date', ''))}"]
    if workout.get("note"):
        lines.append(f"  note: {workout['note']}")
    return "\n".join(lines)

def print_training_log(log):
    """Pretty-print the full training log as a single document."""
    if not log:
        return "Training log is empty."
    out = []
    for w in log:
        out.append(print_workout_summary(w))
        out.append("-" * 60)
    return "\n".join(out)
