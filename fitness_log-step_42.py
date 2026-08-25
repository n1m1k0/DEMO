# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: FitnessLog
import sys

ANSI = sys.stdout.isatty()

def colorize(text, fg, bg=None, bold=False):
    if not ANSI:
        return text
    codes = []
    if bold:
        codes.append("1")
    if fg is not None:
        codes.append(f"3{fg}")
    if bg is not None:
        codes.append(f"4{bg}")
    return f"\033[{','.join(codes)}m{text}\033[0m"

def print_log_header():
    print(colorize("╔══════════════════════════════════════════╗", fg=7, bg=4, bold=True))
    print(colorize("║    F I T N E S S  L O G  -  V E R S I O N  4 2  ║", fg=7, bg=4, bold=True))
    print(colorize("╚══════════════════════════════════════════╝", fg=7, bg=4, bold=True))

def print_log_title(title):
    print(colorize(f"╔══════════════════════════════════════════╗", fg=7, bg=2, bold=True))
    print(colorize(f"║     {title:<45} ║", fg=7, bg=2, bold=True))
    print(colorize("╚══════════════════════════════════════════╝", fg=7, bg=2, bold=True))

def print_exercise(ex):
    print(colorize(f"   {ex['name']:<35}  ", fg=3, bold=True))
    for i, set_data in enumerate(ex['sets'], 1):
        w = set_data['weight']
        reps = set_data['reps']
        if reps:
            print(colorize(f"   {i:>2}. {w:>6} kg  ×  {reps:>4} шт.", fg=3, bold=True))
        else:
            print(colorize(f"   {i:>2}. {w:>6} kg  ×  -", fg=3))

def print_progress(prog):
    print(colorize(f"   📈 Прогресс: {prog['total_sets']:<45}  ", fg=2, bold=True))
    print(colorize(f"   🏋️  Всего упражнений: {prog['total_exercises']}  ", fg=2, bold=True))
    print(colorize(f"   ⏱️  Дата: {prog['date']}  ", fg=2, bold=True))
