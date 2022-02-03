roman_dict = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}


# 1023 = 1000 + 20 + 3 = M + XX + III
# 900 + 80 + 7 = CM + LXXX + VII            -> (10 - 1) * 100 + (5 + 1 + 1 + 1) * 10 + (5 + 1 + 1) * 1
# 1000 + 600 + 90 + 9 = M + DC + XC + IX    -> (1) * 1000 + (5 + 1) * 100 + (10 - 1) * 10 + (10 - 1)
# 10 + 9 = X + IX                           -> (1) * 10 + (10 - 1)
# 4  = IV                                   -> (5 - 1)
# 40 + 4 = XL + IV                          -> (5 - 1) * 10 + (5 - 1)
# 8 = VIII                                  -> (5 + 1 + 1 + 1)

# 1, 2, 3 - I / 4 - IV / 5 - V

# max = 3999

def int_to_Romain(integer: int) -> str:
    string = []
    for pos in range(len(str(integer)) - 1, -1, -1):
        num = integer % 10 ** (pos + 1) - integer % 10 ** pos
        if num == 0:
            continue
        print(f'{num=}')
        count = num // 10 ** pos
        print(f'{count=}')
        base_num = num / count

        if count <= 3:
            for i in range(count):
                string.append(roman_dict[base_num])
        elif count == 4:
            string.append(roman_dict[base_num])
            string.append(roman_dict[base_num * 5])
        elif count == 5:
            string.append(roman_dict[base_num * 5])
        elif 6 <= count <= 8:
            string.append(roman_dict[base_num * 5])
            for i in range(count - 5):
                string.append(roman_dict[base_num])
        elif count == 9:
            string.append(roman_dict[base_num])
            string.append(roman_dict[base_num * 10])

    return ''.join(string)


print(int_to_Romain(10))
