import decimal


def significant_digit_for_uc(in_num, digit):
    str_num = str(in_num)
    offset = 0
    for i in str_num:
        if i == '0' or i == '.':
            offset += 1
            continue
        else:
            break
    # offset 是有效数字的地方（从0开始）
    if digit == 2:
        if decimal.Decimal("%.2g" % decimal.Decimal(str_num)) < decimal.Decimal(str_num):
            return "%.2g" % decimal.Decimal(
                str_num[:offset + 2 + (1 if str_num[offset + 1] == '.' else 0)] + '9' + str_num[offset + 3 + (
                    1 if str_num[offset + 1] == '.' else 0):])
        else:
            return "%.2g" % decimal.Decimal(str_num)
    else:
        if decimal.Decimal("%.1g" % decimal.Decimal(str_num)) < decimal.Decimal(str_num):
            return "%.1g" % decimal.Decimal(
                str_num[:offset + 1 + (1 if str_num[offset + 1] == '.' else 0)] + '9' + str_num[offset + 2 + (
                    1 if str_num[offset + 1] == '.' else 0):])
        else:
            return "%.1g" % decimal.Decimal(str_num)

    # if offset + digit >= len(str_num) or str_num[offset + (1 if str_num[offset + 1] == '.' else 0) + digit] == '0':
    #     pass
    # else:
    #     str_num = str_num[:offset + (1 if str_num[offset + 1] == '.' else 0) + digit] + '9' + str_num[offset + (
    #         2 if str_num[offset + 1] == '.' else 1) + digit:]
    # check_off = 0
    # if digit == 2:
    #     res = "%.2g" % decimal.Decimal(str_num)
    #     is_point = '.' in str_num
    #     for i in res:
    #         if i == '0' or i == '.':
    #             check_off += 1
    #         else:
    #             if check_off + digit + is_point == len(res):
    #                 return res
    #             else:
    #                 return res + '.0' if not is_point else '0'
    # else:
    #     res = "%.1g" % decimal.Decimal(str_num)
    #     is_point = False
    #     for i in res:
    #         if i == '0' or i == '.':
    #             check_off += 1
    #         else:
    #             if check_off + digit + is_point == len(res):
    #                 return res
    #             else:
    #                 return res + '.0' if not is_point else '0'


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
