import logging

logging.basicConfig(level=logging.WARNING)                                        # logging.INFO / سطح نامناسب لاگینگ


class Person():                                                                   # class Person: / اشتباه در تعریف کلاس
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logging.warning("Person created! {} {}".format(self.name, self.family))      # logging.info() / سطح نامناسب لاگینگ

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.critical("Invalid age!")                                         # logging.error() / سطح نامناسب لاگینگ
        self._age = 0

# نبود instance های مربوط به کلاس در اینجا