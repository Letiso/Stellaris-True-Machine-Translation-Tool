from re import finditer


def string_processing(line, file_type, mode):
    return localisation(line, mode) if file_type == 'localisation' else name_list(line, mode)


# Localisation type files
def localisation(line, mode):
    if mode == 'replace':
        symbols_stack = []  # Contains symbols from the list below found in the current string
        symbols = ['\"', '§H', '§L', '§G', '§Y', '§R', '§!', '\\\\n', ]

    # Сохраняем в стек все попавшиеся по очереди символы в строке
        for symbol in symbols:
            for position in finditer(symbol, line):
                symbols_stack.append([position.group(), position.regs[0]])

    # Сортируем элементы стека пузырьком
        symbols_count = len(symbols_stack)
        symbols_stack = symbols_stack

        iteration_index = 0
        while iteration_index < symbols_count - 1:
            current_index = 0
            while current_index < symbols_count - 1 - iteration_index:
                if symbols_stack[current_index][-1][-1] > symbols_stack[current_index + 1][-1][0]:
                    symbols_stack[current_index], symbols_stack[current_index + 1] = symbols_stack[current_index + 1], \
                                                                                     symbols_stack[current_index]
                current_index += 1
            iteration_index += 1

    # Избавляемся от индексов внутри стека
        for index, symbol in enumerate(symbols_stack):
            symbols_stack[index] = symbol[0]

    # Заменяем по одному символы на |
        for symbol in symbols_stack:
            line = line.replace(symbol, '<', 1)

    # передаем строку на перевод
        return line, symbols_stack

    elif mode == 'return':
        symbols_stack = line[-1]
        line = line[0]

    # Убираем пробелы вокруг символа |, которые появляются в следствии обращения к API Google
        line = line.replace(' <', '<').replace('< ', '<')

    # Возвращаем символы в переведенную строку
        for symbol in symbols_stack:
            line = line.replace('<', symbol, 1)

        return line


# Name-list type files
def name_list(line, mode):
    if mode == 'replace':
        symbols_stack = []  # Contains symbols from the list below found in the current string
        symbols = ['\"', ]

    # Сохраняем в стек все попавшиеся по очереди символы в строке
        for symbol in symbols:
            for position in finditer(symbol, line):
                symbols_stack.append([position.group(), position.regs[0]])

    # Сортируем элементы стека пузырьком
        symbols_count = len(symbols_stack)
        symbols_stack = symbols_stack

        iteration_index = 0
        while iteration_index < symbols_count - 1:
            current_index = 0
            while current_index < symbols_count - 1 - iteration_index:
                if symbols_stack[current_index][-1][-1] > symbols_stack[current_index + 1][-1][0]:
                    symbols_stack[current_index], symbols_stack[current_index + 1] = symbols_stack[current_index + 1], \
                                                                                     symbols_stack[current_index]
                current_index += 1
            iteration_index += 1

    # Избавляемся от индексов внутри стека
        for index, symbol in enumerate(symbols_stack):
            symbols_stack[index] = symbol[0]

    # Заменяем по одному символы на |
        for symbol in symbols_stack:
            line = line.replace(symbol, '<', 1)

    # передаем строку на перевод
        return line, symbols_stack

    elif mode == 'return':
        symbols_stack = line[-1]
        line = line[0]

    # Убираем пробелы вокруг символа |, которые появляются в следствии обращения к API Google
        line = line.replace(' <', '<').replace('< ', '<')

    # Возвращаем символы в переведенную строку
        for symbol in symbols_stack:
            line = line.replace('<', symbol, 1)

        return line


