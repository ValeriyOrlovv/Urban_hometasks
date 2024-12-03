class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


class Car:

    def __init__(self, model, _vin, __numbers):
        self.model = model
        self._vin = _vin
        self.__numbers = __numbers
        self.__is_valid_numbers(__numbers)
        self.__is_valid_vin(_vin)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            if vin_number in range(1000000, 10000000):
                if vin_number == self._vin:
                    return True
                return False
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                if numbers == self.__numbers:
                    return True
                return False
            raise IncorrectCarNumbers('Неверная длина номера')
        raise IncorrectCarNumbers('Некорректный тип данных для номеров')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
