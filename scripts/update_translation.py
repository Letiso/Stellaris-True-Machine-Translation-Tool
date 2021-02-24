from copy import copy

from typing import Union, Tuple
from scripts.stack import Stack, NameListElement, LastParentStack


# TODO Добавить обновление всех файлов мода
# Алгоритм запрашивает папку мода с локализациями
# и поочередно для каждого из файлов коллекции ищет совпадения по имени в папке (создаем пары файлов)
# (использование using_chosen_file для всего мода сразу, мы выбираем только папку мода с переводами)

def update_translation(files_for_combine, update_type):
    return localisation_update(files_for_combine[0], files_for_combine[-1].original_file_path, update_type) \
        if files_for_combine[-1].type == 'localisation' \
        else name_list_update(files_for_combine[0], files_for_combine[-1].original_file_path, update_type)


def localisation_update(original_file_path, localisation_file_path, update_type):
    log = False
    with open(original_file_path, 'r', encoding='utf-8') as original_text, \
            open(localisation_file_path, 'r', encoding='utf-8') as localisation_text:
        original_text = original_text.readlines()
        localisation_text = localisation_text.readlines()

    updated_text = copy(original_text)

    for original_index, localisation_index in index_dict(localisation_text, original_text, 'localisation'):
        try:
            if localisation_index is not None:
                updated_text[original_index] = localisation_text[localisation_index]
        except IndexError:
            break

    if updated_text != localisation_text:
        with open(localisation_file_path if update_type in 'internal_way'
                  else original_file_path, 'w', encoding='utf-8') as updated:
            updated.write(''.join(updated_text))
        log = True
    return log


def name_list_update(original_file_path, localisation_file_path, update_type):
    log = False

    return log


def index_dict(old_tr_text, new_ver_text, file_type):

    _index_dict = {index: None for index, var in enumerate(new_ver_text)}

    if file_type == 'localisation':
        new_ver_text_vars = [new_ver_line.split('"')[0] for new_ver_line in new_ver_text]
        old_tr_text_vars = [old_tr_line.split('"')[0] for old_tr_line in old_tr_text]
        for index in _index_dict:
            if new_ver_text_vars[index] in old_tr_text_vars:
                _index_dict[index] = old_tr_text_vars.index(new_ver_text_vars[index])
    else:
        _new_ver_text_parsed, _new_ver_text_instances = lists_parser(new_ver_text)
        _old_ver_text_parsed, _old_ver_text_instances = lists_parser(old_tr_text)
        _index_dict = comparing_lists(_new_ver_text_instances, _old_ver_text_instances, _index_dict)

    return _index_dict.items()


def comparing_lists(old_text: LastParentStack, new_text: LastParentStack, _index_dict: dict) -> dict:
    for instance in new_text:
        old_ver = list(filter(lambda old_ins: instance.full_path == old_ins.full_path, old_text))
        if len(old_ver) == 1:
            _index_dict[instance.index] = old_ver[0].index
        else:
            continue
    return _index_dict


def lists_parser(name_list: list) -> Tuple[dict, list]:
    brace_stack = Stack()
    last_parent_stack = LastParentStack()
    list_of_instances = []
    old_indexes = {}

    def _list_preparing(_name_list: list) -> list:
        res = []
        for index, line in enumerate(_name_list):
            line = _replace_symbols(line)
            if line == '':
                continue
            elif line.lstrip().startswith('#'):
                continue
            else:
                res.append(line)
                old_indexes[len(res)-1] = index
        return res

    def _replace_symbols(line: str) -> str:
        symbols = ['\n', '\t\t\n', '\t\n', '\t', '\ufeff',]
        for sym in symbols:
            if sym in line:
                line = line.replace(sym, '')
        return line

    def _check_statements(line: str) -> bool:
        if line.lstrip().startswith('#'):
            return True
        if not line.lstrip():
            return True
        return False

    def _create_new_instance_of_namelistelement(key: str, parent_key: str, index: int,
                                                full_path: str, value: Union[str, dict, list] = None) -> NameListElement:
        instance = NameListElement(key=key, parent_key=parent_key, index=index, value=value,
                                   full_path=full_path)
        list_of_instances.append(instance)
        return instance

    def _recursion_processing(_name_list: list, index: int = 0) -> Union[dict, tuple]:
        name_dict = {}
        list_of_elements = []
        while index <= len(_name_list)-1:
            line = _name_list[index]
            if _check_statements(line):
                index += 1
                continue

            if '{' in line and '}' in line:
                line = line.replace('{', '')
                line = line.replace('}', '')
                key, value = line.split('=', maxsplit=1)
                if '=' in value:
                    key1, value1 = value.split('=')
                    new_value = {key1: value1}
                    name_dict[key] = new_value
                    instance = _create_new_instance_of_namelistelement(key=key,
                                                                       parent_key=last_parent_stack.get_parent_key(),
                                                                       index=old_indexes[index], value=new_value,
                                                                       full_path=last_parent_stack.get_full_path(key))
                else:
                    name_dict[key] = value
                    instance = _create_new_instance_of_namelistelement(key=key,
                                                                       parent_key=last_parent_stack.get_parent_key(),
                                                                       index=old_indexes[index], value=value,
                                                                       full_path=last_parent_stack.get_full_path(key))
                list_of_elements.append(instance)
                index += 1
                continue

            elif '{' in line:
                key, *_ = line.split('=')
                brace_stack.push('{')
                instance = _create_new_instance_of_namelistelement(key=key,
                                                                   parent_key=last_parent_stack.get_parent_key(),
                                                                   index=old_indexes[index],
                                                                   full_path=last_parent_stack.get_full_path(key))
                list_of_elements.append(instance)

                last_parent_stack.push(instance)

                lines_ahead = []
                next_line = _name_list[index+1]
                if '=' not in next_line and '{' not in next_line and '}' not in next_line:
                    for i in range(index+1, len(_name_list)):
                        next_line = _name_list[i]

                        if '=' not in next_line and '{' not in next_line and '}' not in next_line:
                            lines_ahead.append(next_line)
                        else:
                            if '}' in next_line:
                                index = i+1
                            else:
                                index = i
                            name_dict[key] = lines_ahead
                            instance.value = lines_ahead
                            break
                    else:
                        name_dict[key] = lines_ahead
                        instance.value = lines_ahead
                else:
                    dictionary, index, child = _recursion_processing(_name_list, index+1)
                    #name_dict[key], index = recursion_processing(_name_list, index+1)
                    name_dict[key] = dictionary
                    instance.children.extend(child)

            elif '}' in line:
                brace_stack.pop()
                last_parent_stack.pop()
                return name_dict, index+1, list_of_elements
            elif '=' in line:
                key, value = line.split('=')
                instance = _create_new_instance_of_namelistelement(key=key,
                                                                   parent_key=last_parent_stack.get_parent_key(),
                                                                   index=old_indexes[index], value=value,
                                                                   full_path=last_parent_stack.get_full_path(key))
                list_of_elements.append(instance)
                name_dict[key] = value
                index += 1
                continue
        else:
            return name_dict, index, list_of_elements

    text = _list_preparing(name_list)
    dictionary_of_parsed_name_list: dict = _recursion_processing(text)[0]
    return dictionary_of_parsed_name_list, list_of_instances

