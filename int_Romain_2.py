y = {1000: 'M',
     900: 'CM',
     500: 'D',
     400: 'CD',
     100: 'C',
     90: 'XC',
     50: 'L',
     40: 'XL',
     10: 'X',
     9: 'IX',
     5: 'V',
     4: 'IV',
     1: 'I'
     }


def int_Romain(num: int):
    res_string = ''
    for key, value in y.items():
        if num // key:
            res_string = res_string + (num // key) * y[key]
            num = num % key
    return res_string


print(int_Romain(3444))

