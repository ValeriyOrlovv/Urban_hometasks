class Horse:
    """"Лошадь."""
    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    """Орёл."""
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    """Пегас, наследуется от орла и лошади."""
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()