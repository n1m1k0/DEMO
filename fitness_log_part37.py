# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: FitnessLog
def test_fitness_log():
    from fitness import FitnessLog, Exercise, Set
    log = FitnessLog()
    
    ex1 = Exercise(name="Подтягивания", sets=[])
    set1 = Set(weight=60, reps=5)
    set2 = Set(weight=70, reps=8)
    
    assert Exercise(name="Подтягивания") == Exercise(name="Подтягивания")
    assert set1.weight == 60 and set1.reps == 5
    
    ex1.add_set(set1)
    ex1.add_set(set2)
    assert len(ex1.sets) == 2
    
    log.add_exercise(ex1)
    assert len(log.exercises) == 1
    
    total_sets = sum(len(e.sets) for e in log.exercises.values())
    assert total_sets == 2
    
    assert ex1.name == "Подтягивания"
    assert set1.weight > 0 and set1.reps > 0
