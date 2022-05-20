from numpy import *
import decimal

history = []


# def input_with_history(string: str, his: list):
#     x = input(string)
#     his.append(x)
#     return x

def significant_digit_for_uc(in_num, digit):
    str_num = str(in_num)
    offset = 0
    for i in str_num:
        if i == '0' or i == '.':
            offset += 1
            continue
        else:
            break
    if offset + digit >= len(str_num) or str_num[offset + (1 if str_num[offset + 1] == '.' else 0) + digit] == '0':
        pass
    else:
        str_num = str_num[:offset + (1 if str_num[offset + 1] == '.' else 0) + digit] + '9' + str_num[offset + (
            2 if str_num[offset + 1] == '.' else 1) + digit:]
    check_off = 0
    if digit == 2:
        res = "%.2g" % decimal.Decimal(str_num)
        is_point = '.' in str_num
        for i in res:
            if i == '0' or i == '.':
                check_off += 1
            else:
                if check_off + digit + is_point== len(res):
                    return res
                else:
                    return res + '.0' if not is_point else '0'
    else:
        res = "%.1g" % decimal.Decimal(str_num)
        is_point = False
        for i in res:
            if i == '0' or i == '.':
                check_off += 1
            else:
                if check_off + digit + is_point== len(res):
                    return res
                else:
                    return res + '.0' if not is_point else '0'


def rule_for_uc(in_uc):
    str_uc = str(in_uc)
    for single_char in str_uc:
        if single_char == '.' or single_char == '0':
            continue
        if single_char == '1' or single_char == '2':
            return significant_digit_for_uc(in_uc, 2)
        else:
            return significant_digit_for_uc(in_uc, 1)


def get_decimal_digit(in_num):
    return len(str(in_num).split('.')[1])


def main():
    global history
    history = []
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
    avg = 0
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
        print(f"tp=tp[count - 2]")
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
