import logging
my_format = "%(asctime)s — %(name)-10s — %(levelname)-16s — %(msecs)s — %(message)s"
logging.basicConfig(filename='person.log', format=my_format, level=logging.DEBUG)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logging.info("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.error("Invalid age!")
        self._age = 0


p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)

