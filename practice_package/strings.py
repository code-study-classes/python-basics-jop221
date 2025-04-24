def extract_file_name(full_file_name):
    import os
    base = os.path.basename(full_file_name)
    name = os.path.splitext(base)[0]
    return name


def encrypt_sentence(sentence):
    even_chars = [sentence[i] for i in range(len(sentence)) if i % 2 == 0]
    odd_chars = [sentence[i] for i in range(len(sentence)) if i % 2 == 1]
    return ''.join(even_chars) + ''.join(odd_chars[::-1])


def check_brackets(expression):
    stack = []
    for i, ch in enumerate(expression, 1):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if not stack:
                return i
            stack.pop()
    if stack:
        return -1
    return 0


def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(parts[::-1])


def count_vowel_groups(word):
    vowels = set('aeiouyAEIOUY')
    count = 0
    prev_is_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_is_vowel:
            count += 1
        prev_is_vowel = is_vowel
    return count
