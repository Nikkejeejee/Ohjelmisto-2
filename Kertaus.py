class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f'{self.species} {self.sound}')


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal, bird):
        self.animals.append(animal)
        self.bird.append(bird)
        return

    def make_list(self):
        print("Here's all the animals in the zoo and their sounds:")
        for animal in self.animals:
            animal.make_sound()
            bird.color()


class Bird(Animal):
    def __init__(self, species, sound, color):
        super().__init__(species, sound)
        self.color = color

    def color(self):
        print(f"{self.color}")


animal1 = Animal("Lion", "roars")
animal2 = Animal("Tiger", "growls")
bird1 = Bird("Cuckoo", "Cuckoo", "Brown")

my_zoo = Zoo()

my_zoo.add_animal(animal1)
my_zoo.add_animal(animal2)
my_zoo.add_animal(bird1)

my_zoo.make_list()
