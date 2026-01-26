NUTRISCORE_RANK = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

def nutriscore_value(letter: str) -> int:
    if not letter:
        return 999
    return NUTRISCORE_RANK.get(letter.upper(), 999)
