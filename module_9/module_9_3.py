first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

fist_result = (len(x[0]) - len(x[1]) for x in list(zip(first, second)) if len(x[0]) != len(x[1]))
second_result = (len(second[x]) == len(first[x]) for x in range(len(first)))

print(list(fist_result))
print(list(second_result))