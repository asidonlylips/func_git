from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def processing(self):
        pass

    @abstractmethod
    def write_to_file(self):
        pass


class Converter(File):
    def __init__(self, filename, jsonname):
        self.filename = filename
        self.jsonname = jsonname
        self.processing_data = []
        self.json_data = []
        self.data = []

    def filereader(self):
        with open('t.csv', 'r') as f_read:
            self.data = f_read.readlines()

    def processing(self):
        for f_string in self.data:
            line = f_string.replace(', ', '|').replace('"', '')
            line = line.split(',')
            self.processing_data.append(line)
        headers = self.processing_data[0]
        for i in range(len(self.processing_data)):
            if i != 0:
                self.json_data.append(list(zip(headers, self.processing_data[i])))

    def write_to_file(self):
        with open(self.jsonname, 'w') as f_write:

            f_write.write('{' + '\n \t "DATA": [' + '\n \t\t \n')
            outside_counter = 0
            for i in self.json_data:
                f_write.write('\t\t{')
                outside_counter += 1
                inside_counter = 0
                for a, b in i:
                    inside_counter += 1
                    a = replaces(a)
                    b = replaces(b)
                    f_write.write('\n' + '\t' * 2 + '"{}": "{}"'.format(a, b))
                    if inside_counter < len(i):
                        f_write.write(',')

                f_write.write('\n \t\t }')
                if outside_counter < len(self.json_data):
                    f_write.write(',' + '\n')
            f_write.write('\n \t ] \n}')


def replaces(input_data):
    output_data = input_data.rstrip("\n")
    output_data = output_data.replace('|', ', ')
    return output_data


if __name__ == "__main__":
    filename = input('enter csv file name ')
    jsonname = input('enter json file name ')
    a = Converter(filename, jsonname)
    a.filereader()
    a.processing()
    a.write_to_file()
