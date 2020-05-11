import math
import sys

def QuadEquation(a, b, c):
    ## 実数解の要素を格納するリスト
    RealNumberSolution_list = []

    ## 判別式
    D = b*b - 4*a*c

    ## a = 0のとき一次方程式を解く
    if a == 0:
        x = -c/b
        print(x)
        sys.exit()

    ## Dが負のとき
    if D < 0:
        print('no solutions')
        sys.exit()

    ## 実数解
    square_D = math.sqrt(D)
    x1 = (-b + square_D) / (2*a)
    x2 = (-b - square_D) / (2*a)

    ## Dの値で場合分け
    if D > 0:
        RealNumberSolution_list.append(x1)
        RealNumberSolution_list.append(x2)
    elif D == 0:
        RealNumberSolution_list.append(x1)

    print(RealNumberSolution_list)
    sys.exit()

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

QuadEquation(a, b, c)
