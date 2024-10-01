def custom_write(file_name: str, strings: list) -> dict:
    file = open(file_name, 'a', encoding='utf-8')
    line_count = 0
    res_dict = {}
    for i in range(len(strings)):
        cursor = file.tell()
        file.write(f'{strings[i]}\n')
        line_count += 1
        res_dict[(line_count, cursor)] = strings[i]
    return res_dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
