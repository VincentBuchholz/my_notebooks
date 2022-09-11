import utils

if __name__ == '__main__':
    utils.get_file_names('/home/jovyan/my_notebooks/modules/ex2/ex2','imp_output_filenames.txt')
    utils.get_all_file_names('/home/jovyan/my_notebooks/modules/ex2','imp_output_all_filenames.txt')
    utils.print_line_one(['test1.txt','test2.txt','test3.txt'],)
    utils.print_emails(['test1.txt','test2.txt','test3.txt'])
    utils.write_headlines(['md1.md','md2.md','md3.md'],'imp_output_headlines.txt')
    