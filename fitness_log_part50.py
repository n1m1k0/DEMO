# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: FitnessLog
# ─────────────────────────────────────────────────────────────────────────────
# FitnessLog – финальная полировка
# ─────────────────────────────────────────────────────────────────────────────
def _render_entry_summary(entry: dict) -> str:
    """Формирует читаемую строку-сводку для одного записанного подхода."""
    parts = [
        f"Exercise: {entry.get('exercise', 'N/A')}",
        f"Sets: {entry.get('sets_completed', 0)} / {entry.get('target_sets', 0)}",
        f"Weight: {entry.get('weight_kg', 0):.1f} kg",
        f"Reps: {entry.get('reps_per_set', 0)}",
    ]
    return " | ".join(parts)


def _render_session_summary(session: dict) -> str:
    """Формирует сводку по завершённой сессии тренировки."""
    total_sets = sum(s.get("sets_completed", 0) for s in session.get("entries", []))
    total_weight = sum(
        s.get("weight_kg", 0) * s.get("reps_per_set", 0)
        for s in session.get("entries", [])
    )
    lines = [
        f"Session date: {session.get('date', 'N/A')}",
        f"Total sets: {total_sets}",
        f"Total kg·reps: {total_weight:.1f}",
    ]
    return "\n".join(lines)


def _render_app_footer() -> str:
    """Выводит финальный отчёт программы при завершении работы."""
    return (
        "\n"
        "=" * 60
        + "\n"
        + "FitnessLog – Training Journal"
        + "\n"
        + "=" * 60
        + "\n"
    )
