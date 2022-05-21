from numpy import *
import decimal
from Ruler_For_UC import rule_for_uc, get_decimal_digit
import os


# history = []


# def input_with_history(string: str, his: list):
#     x = input(string)
#     his.append(x)
#     return x


def main():
    tp = [decimal.Decimal('1.84'),
          decimal.Decimal('1.32'),
          decimal.Decimal('1.20'),
          decimal.Decimal('1.14'),
          decimal.Decimal('1.11'),
          decimal.Decimal('1.09'),
          decimal.Decimal('1.08'),
          decimal.Decimal('1.07'),
          decimal.Decimal('1.06'),
          decimal.Decimal('1.05'),
          # from 1 to 10 (n-1)
          ]
    lst = []
    count = 0
    while 1:
        x = input("")
        if x == 'b':
            break
        lst.append(decimal.Decimal(x))
        count += 1
    avg = sum(lst) / count
    part_sum = 0
    for i in lst:
        part_sum += (i - avg) ** 2
    if count - 2 <= 9:
        print(f"tp={tp[count - 2]}")
        ua = tp[count - 2] * sqrt(part_sum / (count * (count - 1)))
    else:
        ua = decimal.Decimal(input('tp:')) * sqrt(part_sum / (count * (count - 1)))
    print(f"ua={ua}")
    ub = eval(input('(ub = delta / C)输入ub: \n'))
    print(f"ub={ub}")
    uc = sqrt(ua ** 2 + decimal.Decimal(str(ub)) ** 2)
    ruled_uc = rule_for_uc(uc)
    print(f"uc={uc} (beta)uc={ruled_uc}")
    print(f"avg={avg} (beta)avg={round(avg, get_decimal_digit(ruled_uc))}")


if os.getenv('--with-debug') == '1':
    main()
