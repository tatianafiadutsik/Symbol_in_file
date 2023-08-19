def symbol_in_file(file, symbol_count, symbol_percent, symbol_all):

    with open(file) as f:
        for line in f:
            symbol_all += (len(line))
            for char in "".join(line.lower().split()):
                if char in symbol_count:
                    symbol_count[char] += 1
                    symbol_percent[char] = (symbol_count[char] * 100) / symbol_all
                else:
                    symbol_count[char] = 1
                    symbol_percent[char] = (symbol_count[char] * 100) / symbol_all

    print(f'В файле {file} содержится следующее количество символов в процентном соотношении:')
    for key, value in sorted(symbol_percent.items()):
        if key != 0:
            print(f'{key} --- {round(value, 2)}%')


file_symbol_count = {}
file_symbol_percent = {}
file_symbol_all = 0
symbol_in_file('about_lorem.txt', file_symbol_count, file_symbol_percent, file_symbol_all)
