# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: FitnessLog
def parse_date(date_str):
    """Парсит дату в формате DD.MM.YYYY или YYYY-MM-DD, возвращает datetime.date."""
    import re
    date_str = date_str.strip()
    if not date_str:
        raise ValueError("Дата не может быть пустой")
    
    # Пытаемся распарсить разные форматы
    patterns = [
        (r'(\d{1,2})\.(\d{1,2})\.(\d{4})', 'dd.mm.yyyy'),
        (r'(\d{1,2})\.(\d{1,2})\.(\d{2})', 'dd.mm.yy'),
        (r'(\d{4})-(\d{1,2})-(\d{1,2})', 'yyyy-mm-dd'),
    ]
    
    for pattern, fmt in patterns:
        match = re.match(pattern, date_str)
        if match:
            groups = match.groups()
            day, month, year = int(groups[0]), int(groups[1]), int(groups[2])
            
            # Корректируем двузначный год
            if len(year) == 2:
                year += 2000
            
            try:
                return datetime.date(year, month, day)
            except ValueError as e:
                raise ValueError(f"Некорректная дата: {date_str} - {e}") from e
    
    # Пытаемся использовать strptime для других форматов
    for fmt in ['%d/%m/%Y', '%d-%m-%Y']:
        try:
            return datetime.datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    
    raise ValueError(f"Не удалось распарсить дату '{date_str}'. Ожидаемый формат: DD.MM.YYYY или YYYY-MM-DD")
