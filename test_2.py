def func(x,y):
    return x+y, x,y


def func_2():
    return func(2,3)

def func_3():
    print(func_2()[0])



func_3()