def insertion_sort(ins):
    for i in range(len(ins)):
        while ins[i-1] > ins[i] and i-1 >= 0:
            ins[i], ins[i-1] = ins[i-1], ins[i]
            i -= 1
    return ins
