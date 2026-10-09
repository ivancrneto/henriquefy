from django.db import models


class Model(models.Model):
    pass


class Base(Model):
    pass


class Order(Base):
    pass


class Mid:
    pass


class Leaf2(Mid):
    pass


class Leaf3(Leaf2):
    pass


class Puppy2(Leaf2):  # henriquefy: ignore[modeling.inheritance-depth]
    pass
