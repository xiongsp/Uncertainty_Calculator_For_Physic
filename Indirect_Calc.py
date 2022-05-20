import sympy as sy
import decimal
import numpy as np

history = []


# def input(string: str, his: list):
#     x = input(string)
#     his.append(x)
#     return x


def main():
    global history
    history = []
    print("不能将单位换成SI！但要保证uc、val单位一致！")
    input_var = input('所含自变量:\n' ).split(' ')
    for i in input_var:
        globals()[i] = sy.symbols(i)
    input_val = input('各自变量读出值:\n' ).split(' ')
    for i in input_val:
        input_val[input_val.index(i)] = decimal.Decimal(i)
    input_uc = input('各自变量绝对不确定度(uc):\n').split(' ')
    for i in input_uc:
        input_uc[input_uc.index(i)] = decimal.Decimal(i)
    input_fun = input('函数:\n')
    input_to_ln = input('是否取对数(1是):\n') == '1'
    origin_fun = eval(input_fun)
    if input_to_ln:
        fun = sy.ln(eval(input_fun))
    else:
        fun = origin_fun

    subs = {}
    part_sum = 0
    for i in input_val:
        subs[input_var[input_val.index(i)]] = i
    for i in input_uc:
        f_diff = sy.diff(fun, input_var[input_uc.index(i)])
        if f_diff.args.__len__() != 0:
            tmp = decimal.Decimal(
                np.format_float_positional((f_diff.subs(subs) / f_diff.args[0]) * i, precision=2, unique=True,
                                           fractional=False, trim='-'))
            part_sum += tmp ** 2 * f_diff.args[0] ** 2
            print(f"{input_var[input_uc.index(i)]} : {f_diff.args[0]}*{tmp}")
        else:
            tmp = decimal.Decimal(
                np.format_float_positional(f_diff.subs(subs) * i, precision=2, unique=True, fractional=False, trim='-'))
            part_sum += tmp ** 2
            print(f"{input_var[input_uc.index(i)]} : {tmp}")
    val = origin_fun.subs(subs)
    result = 0
    try:
        result = part_sum ** 0.5
    except:
        result = part_sum.sqrt()

    if input_to_ln:
        print(f"\n相对不确定度ur: {result*100}%\n函数值: {val}\n绝对不确定度uc:{result * val}")
    else:
        ur = result / val
        print(f"\n相对不确定度ur: {ur * 100}%\n函数值: {val}\n绝对不确定度uc:{result}")
