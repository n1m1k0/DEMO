# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: FitnessLog
import argparse

def main():
    parser = argparse.ArgumentParser(description="FitnessLog CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add-workout")
    add_parser.add_argument("--user-id", type=int, help="ID пользователя")
    add_parser.add_argument("--exercise", help="Название упражнения")
    add_parser.add_argument("--sets", type=float, help="Количество подходов")
    add_parser.add_argument("--reps", type=int, help="Повторений за подход")

    show_parser = subparsers.add_parser("show-workout", required=False)
    show_parser.add_argument("--user-id", type=int)

    parser.parse_args()


if __name__ == "__main__":
    main()
