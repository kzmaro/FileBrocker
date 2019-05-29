import glob, os

file_list = glob.glob('*')

refined_file_list = [i for i in glob.glob('*') if os.path.isfile(i)]

for part in refined_file_list:
    name1 = str(part)
    dot_index = name1.rindex('.')
    ex_rem_name = name1[:dot_index]

    ret_name = ex_rem_name + '.FB'
    print(ret_name)
    os.rename(part, ret_name)
