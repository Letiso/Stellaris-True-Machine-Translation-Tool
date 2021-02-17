from os import path, mkdir

from scripts.utils import local_mod_path


def put_lines(file):
    localisation_path_list = file.original_file_path.split(f'{file.mod_id}\\')[-1].split('\\')[0:-2]
    localisation_name = file.original_file_name.replace("english", file.target_language)
    localisation_path = f'{local_mod_path}'
    index = 0

    for folder in localisation_path_list:
        localisation_path += f'\\{folder}'
        if path.isdir(localisation_path) is False:
            mkdir(localisation_path)
    localisation_path += f'\\{localisation_name}'

    with open(file.original_file_path, 'r', encoding='utf-8') as original, \
            open(file.source_file_path, 'r', encoding='utf-8') as source, \
            open(file.user_input_file_path, 'r', encoding='utf-8') as user_input:
        original = original.readlines()
        source = source.readlines()
        user_input = user_input.readlines()

    with open(f"{localisation_path}", 'w', encoding='utf-8') as localisation:
        if file.type in 'localisation':
            original[0] = original[0].replace('l_english', f'l_{file.target_language}')
        localisation.write('\ufeff')        # It's an adding BOM to usual UTF-8

        for line in original:
            if ':' in line:     # For localisaton file type case
                line_parts = line.split(':', maxsplit=1)
                line_parts[1] = line_parts[1].replace(source[index][:-1], user_input[index][:-1])
                line = ':'.join(line_parts)
            else:               # For name-list file type case
                line = line.replace(source[index][:-1], user_input[index][:-1])
                index += 1
            localisation.write(line)
