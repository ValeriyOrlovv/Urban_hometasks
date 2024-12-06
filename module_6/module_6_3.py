from random import randint


class Animal:
    live = True
    sound = True
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _coords=[0, 0, 0]):
        self._cords = _coords
        self.speed = speed

    def move(self, dx, dy, dz):
        initial_z_coord = self._coords[2]
        self._coords[0] += dx
        self._coords[1] += dy
        self._coords[2] += dz
        if self._cords[2] < 0:
            self._cords[2] = initial_z_coord
            print("It's too deep, I can't dive")


    def get_coords(self):
        print(f'X:{self._coords[0]}, Y:{self._coords[1]}, Z:{self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sory, I'm peaceful :)")
        else:
            print("Be careful I'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs_to_give = randint(1, 4)
        if eggs_to_give > 1:
            print ('Here are {eggs_to_give} eggs for you')
        else:
            print ('Here is {eggs_to_give} egg for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        diving_speed = self.speed / 2
        self._cords[2] -= abs(dz)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird):
    sound = 'Click-click-click'

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
# db.attack()

# db.move(1, 2, 3)
# db.get_cords()
# db.dive_in(6)
# db.get_cords()

# db.lay_eggs()