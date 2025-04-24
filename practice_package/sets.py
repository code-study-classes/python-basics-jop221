def find_common_elements(set1, set2):
    result = set()
    for item in set1:
        if item in set2:
            result.add(item)
    return result


def is_superset(set_a, set_b):
    for item in set_b:
        if item not in set_a:
            return False
    return True


def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def count_unique_words(text):
    words = text.lower().split()
    return len(set(words))


def find_shared_items(*sets):
    if not sets:
        return set()
    result = sets[0].copy()
    for s in sets[1:]:
        result = {item for item in result if item in s}
    return result
