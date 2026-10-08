class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass


class Puppy(Dog):
    pass


class ZooError(Exception):
    pass


class NotFound(ZooError):
    pass
