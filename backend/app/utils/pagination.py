def paginate(query, *, page: int = 1, page_size: int = 20):
    total = query.count()
    items = query.limit(page_size).offset((page - 1) * page_size).all()
    return {"items": items, "total": total, "page": page, "page_size": page_size}
