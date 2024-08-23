# Задание со словарём

my_dict = {'Masha': 1998, 'Pasha': 1999, 'Sasha': 2001, 'Dasha': 1987}
print(my_dict)
print(my_dict['Dasha'])
print(my_dict.get('Danya'))
my_dict.update({'sergey': 1964, 'Andrey': 1990})
pasha_birthday = my_dict.pop('Pasha')
print(pasha_birthday)
print(my_dict)

# Задание с множеством

my_set = {1, 2, 2, 3, 65, 3, 5.5, 5.5, 'something'}
print(my_set)
my_set.remove('something')
print(my_set)
