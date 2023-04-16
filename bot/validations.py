def validation_code(code: str) -> bool:
    if not code.isdigit():
        return False
    if len(code) != 9:
        return False
    return True
