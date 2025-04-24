def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


def check_odd_three(number):
    abs_num = abs(number)
    return 100 <= abs_num <= 999 and abs_num % 2 == 1


def check_unique_digits(number):
    abs_num = abs(number)
    if not (100 <= abs_num <= 999):
        return False
    digits = str(abs_num)
    return len(set(digits)) == 3


def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(number):
    abs_num = abs(number)
    if not (100 <= abs_num <= 999):
        return False
    digits = str(abs_num)
    return digits[0] < digits[1] < digits[2]
