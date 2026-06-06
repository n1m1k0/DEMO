# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: FitnessLog
class Exercise:
    def __init__(self, name: str):
        if not name or not isinstance(name, str):
            raise ValueError("Имя упражнения должно быть непустой строкой")
        self.name = name

class WorkoutSet:
    def __init__(self, exercise: Exercise, reps: int, weight: float):
        if not isinstance(exercise, Exercise):
            raise TypeError("Упражнение должно быть экземпляром класса Exercise")
        if reps <= 0 or not isinstance(reps, int):
            raise ValueError("Количество повторений должно быть положительным целым числом")
        if weight <= 0 or not isinstance(weight, (int, float)):
            raise ValueError("Вес должен быть положительным числом")
        self.exercise = exercise
        self.reps = reps
        self.weight = weight

class Workout:
    def __init__(self, date: str):
        if not date or not isinstance(date, str):
            raise ValueError("Дата тренировки должна быть непустой строкой")
        self.date = date
        self.sets = []

    def add_set(self, set_data: dict):
        exercise_name = set_data.get('exercise')
        reps = set_data.get('reps')
        weight = set_data.get('weight')

        if not all([isinstance(exercise_name, str), isinstance(reps, int), isinstance(weight, (int, float))]):
            raise ValueError("Некорректные данные для добавления подхода")

        exercise = Exercise(exercise_name)
        set_obj = WorkoutSet(exercise, reps, weight)
        self.sets.append(set_obj)
