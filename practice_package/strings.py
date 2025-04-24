def extract_file_name(full_file_name):
    import os
    base = os.path.basename(full_file_name)
    # Remove all extensions, not just last
    while True:
        base, ext = os.path.splitext(base)
        if not ext:
            break
    return base


def encrypt_sentence(sentence):
    # Encrypt by taking characters at odd indices, then even indices reversed
    odd_chars = [sentence[i] for i in range(1, len(sentence), 2)]
    even_chars = [sentence[i] for i in range(0, len(sentence), 2)]
    return ''.join(odd_chars) + ''.join(even_chars[::-1])


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
        # Return position of first unmatched '(' as per test expectation
        return stack[0]
    return 0


def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(parts[::-1])


def count_vowel_groups(word):
    vowels = set('aeiouAEIOU')  # Exclude 'y' as vowel
    count = 0
    prev_is_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_is_vowel:
            count += 1
        prev_is_vowel = is_vowel
    return count
