from manager import Context_manager,write_to_file,read_file


def sort_by_length(args):
   return sorted(args.split(','), key=len)


input_information = sort_by_length(read_file('1.txt'))
write_to_file('2.txt', 'x', input_information)   