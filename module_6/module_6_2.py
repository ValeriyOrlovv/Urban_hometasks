class Vehicle:
    """Любой транспорт."""
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(
        self,
        owner: str,
        _model: str,
        __color: str,
        __engine_power: int
    ):
        self.owner = owner
        self._model = _model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self) -> str:
        return f'Модель: {self._model}'

    def get_horsepower(self) -> str:
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self) -> str:
        return f'Цвет: {self.__color}'

    def set_color(self, new_color) -> str:
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')



class Sedan(Vehicle):
    """Класс седан."""
    __PASSANGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()