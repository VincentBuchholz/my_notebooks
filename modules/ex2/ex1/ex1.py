import csv
import platform
import argparse

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line.strip().split(','))
        
def write_list_to_file(output_file, *strings):
    
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(['header'])
        
        for string in strings:
            output_writer.writerow([string])

def read_csv():
    parser = argparse.ArgumentParser(description = 'Add path as arg, to print given file to a new file wirte --file and add file, otherwise the content will be printed')
    parser.add_argument('path', help = 'Path to file')
    parser.add_argument('--file', help = 'file to write to')
      
    args = parser.parse_args()
    
    with open(args.path) as f_obj:
        content = f_obj.readlines()
    
    lst = [line.strip() for line in content]
    

    if args.file == None:
        print(lst)
    else:
         with open(args.file, 'w') as output_file:
            output_writer = csv.writer(output_file)
        
            for string in lst:
                output_writer.writerow([string])

            
if __name__ == '__main__':
    #print_file_content('test.csv')
    #write_list_to_file('test.csv','test1','test2','test3')
    read_csv()

