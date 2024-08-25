MY_LIST = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
INDEX = 0

while INDEX <= len(MY_LIST):
    if MY_LIST[INDEX] > 0:
        print(MY_LIST[INDEX])
        INDEX += 1
    elif MY_LIST[INDEX] == 0:
        INDEX += 1
        continue
    else:
        break
