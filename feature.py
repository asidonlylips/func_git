from calendar import isleap
from manager import Context_manager,write_to_file,read_file


def is_leap_year_v1(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_leap_year_v2(year):
    return True if isleap(year) else False  


def insertion_sort(ins):
    for i in range(len(ins)):
        while ins[i-1] > ins[i] and i-1 >= 0:
            ins[i], ins[i-1] = ins[i-1], ins[i]
            i -= 1
    return ins


def max_duplicate_element(args):
    args = args.split(',')
    count_list = [args.count(i) for i in args]
    max_repeat_index = count_list.index(max(count_list))
    return args[max_repeat_index]


input_information = max_duplicate_element(read_file('1.txt'))
write_to_file('2.txt', 'x', input_information)   


def sort_by_length(args):
   return sorted(args.split(','), key=len)


input_information = sort_by_length(read_file('1.txt'))
write_to_file('2.txt', 'x', input_information)


def new_dict(args1, args2, diction = None):
        dictionary = dict(zip(args1, args2))
        if isinstance(diction, dict):
            dictionary={**dictionary,**diction}
        return dictionary

      
def last_numbers_of_row(numb):
    numbers = [i for i in range(1, numb+1)]
    squares = map(lambda a: a**a, numbers)
    b = str(sum(squares))
    return (b[-10:])
