def is_weekend(day):
    return day in (6, 7)


def get_discount(amount):
    if amount >= 5000:
        return amount * 0.10
    elif amount >= 1000:
        return amount * 0.05
    else:
        return 0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    if 1 <= n <= 9:
        digits = "однозначное"
    elif 10 <= n <= 99:
        digits = "двузначное"
    else:
        digits = "трехзначное"
    return f"{parity} {digits} число"


def convert_to_meters(unitNumber, lengthInUnits):
    units = {
        1: 0.1,    # дециметр
        2: 1000,   # километр
        3: 1,      # метр
        4: 0.001,  # миллиметр
        5: 0.01    # сантиметр
    }
    return lengthInUnits * units.get(unitNumber, 0)


def describe_age(age):
    # Russian number to words for 20-100 (simplified)
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто", "сто"]

    def age_to_words(n):
        if n == 100:
            return "сто"
        t = n // 10
        o = n % 10
        if t == 1:
            teens = {
                10: "десять",
                11: "одиннадцать",
                12: "двенадцать",
                13: "тринадцать",
                14: "четырнадцать",
                15: "пятнадцать",
                16: "шестнадцать",
                17: "семнадцать",
                18: "восемнадцать",
                19: "девятнадцать"
            }
            return teens[n]
        else:
            return (tens[t] + (" " + ones[o] if o > 0 else "")).strip()

    word_age = age_to_words(age)

    # Determine correct declension
    if 11 <= age % 100 <= 14:
        suffix = "лет"
    else:
        last_digit = age % 10
        if last_digit == 1:
            suffix = "год"
        elif 2 <= last_digit <= 4:
            suffix = "года"
        else:
            suffix = "лет"

    return f"{word_age} {suffix}"
