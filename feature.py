def insertion_sort(ins):
    for i in range(len(ins)):
        j = i - 1
        temp = ins[i]
        while ins[j] > temp and j >= 0:
            ins[j + 1] = ins[j]
            j -= 1
        ins[j + 1] = temp
    return ins
