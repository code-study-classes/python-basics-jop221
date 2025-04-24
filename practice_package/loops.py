def sum_even_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)


def count_vowel_triplets(text):
    vowels = set('aeiouy')  
    count = 0
    text = text.lower()
    i = 0
    while i < len(text) - 2:
        if all(ch in vowels for ch in text[i:i + 3]):
            count += 1
            i += 1  # Count overlapping triplets
        else:
            i += 1
    return count


def find_fibonacci_index(number):
    if number < 1:
        return -1
    a, b = 1, 1
    index = 2
    if number == 1:
        return 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for ch in string[1:]:
        if ch != result[-1]:
            result.append(ch)
    return ''.join(result)
