# === Stage 43: Добавь пагинацию длинных списков ===
# Project: FitnessLog
def paginate(items, page_size=10):
    total_pages = (len(items) + page_size - 1) // page_size if page_size else 0
    if total_pages == 0:
        return {"items": [], "page": 1, "page_size": 0, "total_pages": 0, "total": 0}
    page = max(1, min(page_size, total_pages))
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "total": len(items),
    }
