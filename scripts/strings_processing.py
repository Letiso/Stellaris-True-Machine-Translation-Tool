from re import finditer


def string_processing(line, symbols_stack, file_type, mode):
    return localisation(line, symbols_stack, mode) if file_type == 'localisation' \
        else name_list(line, symbols_stack, mode)


# Localisation type files
def localisation(line, symbols_stack, mode):
    symbols = ('§H', '§L', '§G', '§Y', '§R', '§!', '\£', '\$', '\n', '\\\\n', )

    if mode == 'replace':
        line, symbols_stack = replacing(line, symbols, symbols_stack)

    elif mode == 'return':
        line = returning(line, symbols_stack)

    return line, symbols_stack


# Name-list type files
def name_list(line, symbols_stack, mode):
    symbols = ['\"', ]

    if mode == 'replace':
        line, symbols_stack = replacing(line, symbols, symbols_stack)

    elif mode == 'return':
        line = returning(line, symbols_stack)

    return line, symbols_stack


# Processing
def replacing(line, symbols, symbols_stack):
    # Сохраняем в стек все попавшиеся по очереди символы в строке, сохраняя индексы
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


def returning(line, symbols_stack):
    # Убираем пробелы вокруг символа |, которые появляются в следствии обращения к API Google
    line = line.replace(' <', '<').replace('< ', '<')

    # Возвращаем символы в переведенную строку
    for symbol in symbols_stack:
        line = line.replace('<', symbol, 1)

    return line
