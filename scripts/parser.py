"""
                              ↓ Инициализация данных ↓
"""

from re import compile
from shutil import copyfile

from scripts.utils import write_data_about_file, create_temp_folder, data, prepare_temp_files

"""
                              ↓ Парсинг файлов ↓
"""


def search_for_necessary(file_type, line):
    subs = {
        'localisation': compile(': |:0|:1|:"'),
        'name_lists': compile('\t\t|\t"|= ')
    }

    if subs[file_type].search(line) is not None:
        return True
    else:
        return False


def search_for_unnecessary(file_type, line):
    subs = {
        'localisation': compile('#'),
        'name_lists': compile('[#{}]')
    }

    if subs[file_type].search(line) is None:
        return True
    else:
        return False


def strings_parsing(original_file_path, file_type):
    source_text = []
    with open(original_file_path, 'r', encoding='utf-8') as original_text:
        original_text = original_text.readlines()
        for line in original_text:
            if search_for_necessary(file_type, line) and search_for_unnecessary(file_type, line):
                symbol = '\t' if '\t' in line else line.find('"')

                if type(symbol) is not int:
                    prepared_line = line.split(symbol)[-1]

                    if prepared_line[0].islower():
                        # Если первая буква строки не является заглавной,
                        # то есть перед необходимым текстом имеются ненужные элементы

                        quote_symbol = line.find('\"') - 1
                        # Если в строке есть '"',
                        # то делаем срез от начала кавычки до конца строки

                        letter_symbol = line.find('=') + 2
                        # Если в строке нет кавычки, но есть '=',
                        # если первая буква после '=' является заглавной,
                        # то делаем срез от начала первой буквы до конца строки

                        prepared_line = line[quote_symbol + 1:] if '\"' in line \
                            else line[letter_symbol if line[letter_symbol].isupper()
                                      else -1:]
                        # В противном случае оставляем только '\n'
                else:
                    prepared_line = line[symbol + 1:-1]
                    # На случай, если в начале строки нет отступов, в ней наверняка есть кавычки
                source_text.append(prepared_line if prepared_line.endswith('\n') else f'{prepared_line}\n')
            else:
                source_text.append('\n')

    return original_text, source_text


"""
                                ↓ Создание временных файлов ↓
"""


def parser_main(mod_path, mod_id, file_path):
    temp_folder = create_temp_folder(mod_id, file_path)
    write_data_about_file(temp_folder, file_path)
    copyfile(f'{mod_path}\\{file_path}', data["original_file_path"])

    file_type = 'localisation' if '.yml' in data["original_file_name"] else 'name_lists'
    original_text, source_text = strings_parsing(data["original_file_path"], file_type)

    prepare_temp_files(original_text, source_text, file_type, None)
