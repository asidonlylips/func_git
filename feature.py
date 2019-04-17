def feature6(numb):
    numbers = [i for i in range(1, numb+1)]
    squares = map(lambda a: a**a, numbers)
    b = str(sum(squares))
    return (b[-10:])
