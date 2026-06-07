# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: FitnessLog
class FitnessLog:
    def __init__(self):
        self.workouts = []

    def add_workout(self, date, exercises):
        workout = {
            "date": date,
            "exercises": exercises
        }
        self.workouts.append(workout)
        return workout

    def add_exercise(self, workout_date, name, sets=None, reps=None, weight=None):
        if not any(w["date"] == workout_date for w in self.workouts):
            self.add_workout(workout_date, [])
        for w in self.workouts:
            if w["date"] == workout_date:
                if name not in w["exercises"]:
                    w["exercises"][name] = []
                w["exercises"][name].append({
                    "sets": sets or [],
                    "reps": reps,
                    "weight": weight
                })
                return True
        return False

    def get_workouts(self):
        return self.workouts

    def get_exercise_history(self, exercise_name):
        history = []
        for workout in self.workouts:
            if exercise_name in workout["exercises"]:
                history.append({
                    "date": workout["date"],
                    "data": workout["exercises"][exercise_name]
                })
        return history

    def get_progress(self, exercise_name):
        history = self.get_exercise_history(exercise_name)
        if not history:
            return []
        weights = []
        for entry in history:
            for set_data in entry["data"]:
                if set_data.get("weight"):
                    weights.append(set_data["weight"])
        return weights
