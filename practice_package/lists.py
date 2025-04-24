def square_odds(numbers):
    return [x * x for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    def is_valid(email):
        if len(email) < 5:
            return False
        if email.count('@') != 1:
            return False
        if email.startswith('@') or email.endswith('@'):
            return False
        return True
    return [email for email in emails if is_valid(email)]


def filter_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def find_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix
