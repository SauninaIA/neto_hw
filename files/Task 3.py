import os

FILE_CATALOG = "not sorted"
BASE_PATH = os.getcwd()
PATH = os.path.join(BASE_PATH, FILE_CATALOG)

files_list = os.listdir(PATH)


def lines_counter(file_name):
    with open(os.path.join(PATH, file_name), encoding='utf-8') as file:
        length = len(file.readlines())
    return length


def files_dict_func(files):
    files_dict = {}
    for file in files:
        file_info = []
        file_info.append(lines_counter(file))
        with open(os.path.join(PATH, file), encoding='utf-8') as file_obj:
            text = file_obj.read()
        file_info.append(text)
        files_dict[file] = file_info
    return files_dict


def final_entry(files_dict):
    with open(os.path.join(BASE_PATH, 'final.txt'), 'a', encoding='utf-8') as final_file:
        length_list = []
        for file in files_dict:
            length_list.append(files_dict[file][0])
        length_list.sort()
        while length_list != []:
            for file in files_dict:
                if files_dict[file][0] == length_list[0]:
                    text = f'{files_dict[file][1]}\n'
                    final_file.write(f'{file}\n')
                    final_file.write(f'{str(length_list[0])}\n')
                    final_file.write(text)
                    length_list.pop(0)
    return


final_entry(files_dict_func(files_list))