# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: FitnessLog
class FitnessLogError(Exception): pass

def test_edge_cases():
    """Тесты ошибок и пограничных случаев."""
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))

    from fitness_log import (
        Workout, Exercise, Set, User, ProgressTracker, FitnessLog,
        FitnessLogError, parse_workout_file
    )

    # --- 1. Неверный формат файла ---
    with open('/tmp/test_bad_format.txt', 'w') as f:
        f.write('This is not a valid workout file\n')
    try:
        parse_workout_file('/tmp/test_bad_format.txt')
        assert False, "Expected FitnessLogError"
    except FitnessLogError:
        pass

    # --- 2. Упражнение без названия ---
    ex = Exercise(name='', sets=[], rest_min=0)
    workout = Workout(exercises=[ex])
    try:
        workout.validate()
        assert False, "Expected ValueError"
    except (ValueError, FitnessLogError):
        pass

    # --- 3. Отрицательные веса ---
    ex2 = Exercise(name='Push-up', sets=[Set(reps=10, weight=-5, rest_min=0)])
    workout2 = Workout(exercises=[ex2])
    try:
        workout2.validate()
        assert False, "Expected ValueError"
    except (ValueError, FitnessLogError):
        pass

    # --- 4. Ноль повторений ---
    ex3 = Exercise(name='Squat', sets=[Set(reps=0, weight=50, rest_min=60)])
    workout3 = Workout(exercises=[ex3])
    try:
        workout3.validate()
        assert False, "Expected ValueError"
    except (ValueError, FitnessLogError):
        pass

    # --- 5. Дубликат упражнения в одной сессии ---
    ex4a = Exercise(name='Bench', sets=[Set(reps=10, weight=60, rest_min=2)])
    ex4b = Exercise(name='Bench', sets=[Set(reps=8, weight=70, rest_min=3)])
    workout4 = Workout(exercises=[ex4a, ex4b])
    try:
        workout4.validate()
        assert False, "Expected ValueError"
    except (ValueError, FitnessLogError):
        pass

    # --- 6. Пустой файл прогресса ---
    pt = ProgressTracker()
    assert len(pt.records) == 0

    # --- 7. Неверный email при регистрации ---
    try:
        user_bad = User('test', 'bad-email')
        assert False, "Expected ValueError"
    except (ValueError, FitnessLogError):
        pass

    # --- 8. Логирование пустого упражнения ---
    log = FitnessLog()
    ex5 = Exercise(name='Test', sets=[])
    try:
        log.add_workout(Workout(exercises=[ex5]))
        assert False, "Expected ValueError"
    except (ValueError, FitnessLogError):
        pass

    print("All edge case tests passed!")
