from manager import Context_manager


class Csv_to_json:
    def __init__(self):
        self.filename = None
        self.jsonfile = None
    
    def reader(self):
        with Context_manager(self.filename, 'r') as f_read:
            data = []
            headers = f_read.readline().replace('\n','').split(',')
            for line in f_read.readlines():
                data.append(list(zip(headers,line.replace('\n','').split(','))))
            return data

    def write_to_json(self, data):
        with Context_manager(self.jsonfile, 'a') as f_write:
            f_write.write('{ \n')
            f_write.write('\t'+'"INFORMATION":' + ' [' + '\n')
            for i in range(len(data)):
                f_write.write('\n'+'\t'*2 +"{"+'\n')
                for j in range (len(data[0])):
                    f_write.write('\t'*3+str(data[i][j]).replace("(","").replace(")","").replace(","," :").replace("'",'"')+"\n")
                f_write.write('\n'+'\t\t' + "}")
            f_write.write('\n' + '\t' + ' ]' + '\n')
            f_write.write('}')

            
        



if __name__ == "__main__":
    convert = Csv_to_json()
    convert.filename = input("enter name of .csv file ")
    convert.jsonfile = input("enter name of .json file ")
    data = convert.reader()
    convert.write_to_json(data)
    

            


