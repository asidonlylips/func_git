from manager import Context_manager,write_to_file,read_file


def max_duplicate_element(args):
    args = args.split(',')
    count_list = [args.count(i) for i in args]
    max_repeat_index = count_list.index(max(count_list))
    return args[max_repeat_index]


input_information = max_duplicate_element(read_file('1.txt'))
write_to_file('2.txt', 'x', input_information)   