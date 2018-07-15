# Assuming for Python 3.6 and above that dictionaries retain their order during iteration

reference = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
             4: 'IV', 1: 'I'}


def roman_numeralize(num):

    result = ''

    for key, val in reference.items():
        if num == 0:
            break
        elif num >= key:
            floored = num // key
            result += floored * val
            num -= floored * key

    return result


print(roman_numeralize(2018))