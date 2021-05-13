from person import Person                                   # هیچگونه نیازی به این عملیات در این فایل مشاهده نمی شود
import logging

logging.basicConfig(level=logging.INFO)                              # logging.DEBUG / سطح نامناسب لاگینگ


def sub(a, b):
    if b != 0:
        return a / b                                        # logging.debug("a/b=" + str(a / b))  باید به خط پایین برود
        logging.debug("a/b=" + str(a / b))                      # return a / b   / باید به خط بالا برود
    logging.info("Divide by zero!")                             # logging.error() / سطح نامناسب لاگین


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)                         # مربوط به فایل person
p2 = Person("gholi", "gholami", -23)                         # مربوط به فایل person
