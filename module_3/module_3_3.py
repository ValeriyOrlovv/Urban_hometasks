def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    

values_list = [423, 'Goodle', None]
values_list_2 = [54.32, 'Строка']
values_dict = {
    'a': 4,
    'b': 'Python',
    'c': False
}

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)