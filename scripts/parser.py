from re import compile
from shutil import copyfile

from scripts.utils import write_data_about_file, create_temp_folder, data, prepare_temp_files


def parser_main(mod_path, mod_id, file_path):
    temp_folder = create_temp_folder(mod_id, file_path)
    write_data_about_file(temp_folder, file_path)
    copyfile(f'{mod_path}\\{file_path}', data["original_file_path"])

    file_type = 'localisation' if '.yml' in data["original_file_name"] else 'name_lists'
    original_text, source_text = localisation(data["original_file_path"]) if file_type == 'localisation' \
                            else name_list(data["original_file_path"])

    prepare_temp_files(source_text)


def search(subs, line, exists_or_not):   # For necessary & unnecessary parts of target line
    if bool(subs.search(line)) == exists_or_not:
        return True
    else:
        return False


def localisation(original_file_path, subs_necessary=compile(': |:0|:1|:"'), subs_unnecessary=compile('#')):
    source_text = []
    with open(original_file_path, 'r', encoding='utf-8') as original_text:
        original_text = original_text.readlines()

        for line in original_text:
            if search(subs_necessary, line, True) and search(subs_unnecessary, line, False):
                # If necessary parts does exist and unnecessary parts does not exist at target string
                symbol = line.find('"')

                if line.endswith('\n'):
                    line = line.rsplit('\n', 1)[0]
                line = line[symbol + 1:-1]

                source_text.append(f'{line}\n')
            else:
                source_text.append('\n')

    return original_text, source_text


def name_list(original_file_path, subs_necessary=compile('\t\t|\t"|= '), subs_unnecessary=compile('[#{}]')):
    source_text = []
    with open(original_file_path, 'r', encoding='utf-8') as original_text:
        original_text = original_text.readlines()

        for line in original_text:
            if search(subs_necessary, line, True) and search(subs_unnecessary, line, False):
                # If necessary parts does exist and unnecessary parts does not exist at target string
                symbol = '\t'

                line = line.split(symbol)[-1]   # Большинство строк проходят сразу

                if line[0].islower():
                    # Если первая буква строки не является заглавной,
                    # то есть перед необходимым текстом имеются ненужные элементы

                    quote_symbol = line.find('\"') - 1
                    # Если в строке есть '"',
                    # то делаем срез от начала кавычки до конца строки

                    letter_symbol = line.find('=') + 2
                    # Если в строке нет кавычки, но есть '=',
                    # если первая буква после '=' является заглавной,
                    # то делаем срез от начала первой буквы до конца строки

                    line = line[quote_symbol:] if '\"' in line \
                        else line[letter_symbol if line[letter_symbol].isupper()
                                  else -1:]
                    # В противном случае оставляем только '\n'

                source_text.append(line)
            else:
                source_text.append('\n')

    return original_text, source_text
