def feature1(args):
    count_list = [args.count(i) for i in args]
    max_repeat_index = count_list.index(max(count_list))
    return args[max_repeat_index]
