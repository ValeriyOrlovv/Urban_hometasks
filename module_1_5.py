immutable_var = (1, 2, 'a', 'b')
print(immutable_var)

# immutable_var[0] = 48:
# Упадёт исклюбчение,
# поскольку в кортеже содержаться неизменяемые типы данных

mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[0] = 'one'
print(mutable_list)
