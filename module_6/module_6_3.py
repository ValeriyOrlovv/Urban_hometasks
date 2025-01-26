from random import randint
from re import L


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords=[0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        initial_dz = self._cords[2]
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] < 0:
            self._cords[2] = initial_dz
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = randint(1, 4)
        if eggs > 1:
            print(f'Here are {eggs} eggs for you')
        else:
            print(f'Here is {eggs} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed // 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
