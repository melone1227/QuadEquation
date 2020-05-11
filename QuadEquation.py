import math

def QuadEquation(a, b, c):
    ## 実数解の要素を格納するリスト
    RealNumberSolution_list = []

    ## 判別式
    D = b*b - 4*a*c

    ## a = 0のとき一次方程式を解く
    if a == 0:
        x = -c/b
        print(x)
        return 0

    ## 実数解
    square_D = math.sqrt(D)
    x1 = (-b + square_D) / (2*a)
    x2 = (-b - square_D) / (2*a)

    ## Dの正負で場合分け
    if D > 0:
        RealNumberSolution_list.append(x1)
        RealNumberSolution_list.append(x2)
    elif D == 0:
        RealNumberSolution_list.append(x1)
    else:
        print('no solutions')

    print(RealNumberSolution_list)
    return 0

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

QuadEquation(a, b, c)