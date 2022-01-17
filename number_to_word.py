dictionary = {
    1: "bir",
    2: "ikki",
    3: "uch",
    4: "to'rt",
    5: "besh",
    6: "olti",
    7: "yetti",
    8: "sakkiz",
    9: "to'qqiz",
    10: "o'n",
    20: "yigirma",
    30: "o'ttiz",
    40: "qirq",
    50: "ellik",
    60: "oltmish",
    70: "yetmish",
    80: "sakson",
    90: "to'qson",
    100: "yuz",
    1000: "ming",
    1000000: "million",
    1000000000: "milliard",
    1000000000000: "trillion",
    10 ** 15: "kvadrillion",
    10 ** 18: "kvintillion",
    10 ** 21: "sekstillion",
    10 ** 24: "septillion",
    10 ** 27: "oktillion",
    10 ** 30: "nonillion",
    10 ** 33: "desillion",
    10 ** 36: "andesillion",
    10 ** 39: "duadesillion",
    10 ** 42: "tridesillion",
    10 ** 45: "qvadridesillion",
    10 ** 48: "kvindesillion",
    10 ** 51: "seksdesillion",
    10 ** 54: "septendesillion",
    10 ** 57: "oktadesillion",
    10 ** 60: "novemdesillion",
    10 ** 63: "vijintillion",
    10 ** 66: "unvijintillion",
    10 ** 69: "dvavijintillion",
    10 ** 72: "trivijintillion",
    10 ** 75: "kvadrivijintillion",
    10 ** 78: "kvinvijintillion",
    10 ** 81: "seksvijintillion",
    10 ** 84: "septavijintillion",
    10 ** 87: "oktavijintillion",
    10 ** 90: "novemvijintillion",
    10 ** 93: "trijintillion",
    10 ** 96: "antrijintillion",
    10 ** 99: "dvatrijintillion",
    10 ** 100: "gogol",
}

def lower_bounder(n: int) -> int:
    if n == (n // 3) * 3 + 1:
        return n
    if n == (n // 3) * 3 + 2 or n == (n // 3) * 3 - 1:
        return n - 1
    if n == (n // 3) * 3 + 3  or n == (n // 3) * 3 :
        return n - 2

def reader(k):
    d = lower_bounder(len(str(k)))
    if k == 0:
        return ""
    if len(str(k)) == 1:
        return f"{dictionary[k]}"
    if len(str(k)) == 2:
        return f"{dictionary[k - k % 10]} " \
               f"{reader(k % 10)}"
    if len(str(k)) == 3:
        return f"{dictionary[(k - k % 100) // 100]} " \
               f"{dictionary[(k - k % 100) // ((k - k % 100) // 100)]} " \
               f"{reader(k % 100)}"
    if d <= len(str(k)) <= d + 2:
        return f"{reader((k - k % (10 ** (d - 1))) // (10 ** (d - 1)))} " \
               f"{dictionary[(k - k % (10 ** (d - 1))) // ((k - k % (10 ** (d - 1))) // (10 ** (d - 1)))]} " \
               f"{reader(k % (10 ** (d - 1)))}"

def num_to_word(number: int) -> str:
    try:
        if number == 0:
            return "nol"
        else:
            return reader(number)
    except:
        return "something went wrong"
