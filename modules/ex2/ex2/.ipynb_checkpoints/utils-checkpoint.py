import os

def get_file_names(folderpath,out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    with open(out,'w') as file:
        for f in os.listdir(folderpath):
            if os.path.isfile(f):
                file.write(f +'\n')
            
def get_all_file_names(folderpath,out='output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    with open(out,'w') as file:
        for path,dirs,files in os.walk(folderpath):
            for name in files:
                file.write(os.path.join(path, name)+'\n')

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in file_names:
        with open (file) as f:
            print(f.readline().rstrip())
            
def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file in file_names:
        with open (file) as f:
            lines = f.readlines()
            
        for line in lines:
            if '@' in line:
                print(line.strip())
                
def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    with open(out,'w') as output:
        for file in md_files:
            with open (file) as f:
                lines = f.readlines()
            
                for line in lines:
                    if line[0].strip() =='#':
                        output.write(line.strip()+'\n')
   
    
if __name__ == '__main__':
    #get_all_file_names('/home/jovyan/my_notebooks/modules/ex2')
    #print_line_one(['test1.txt','test2.txt','test3.txt'])
    #print_emails(['test1.txt','test2.txt','test3.txt'])
    write_headlines(['md1.md','md2.md','md3.md'])