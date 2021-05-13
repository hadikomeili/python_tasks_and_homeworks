# from person import Person
import logging


logger = logging.getLogger()
#=====================================================
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('sample.log')
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)
#=====================================================
stream_format = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_format = logging.Formatter("%(asctime)s — %(name)-10s — %(levelname)-16s — %(msecs)s — %(message)s")
file_handler.setFormatter(file_format)
stream_handler.setFormatter(stream_format)
#=====================================================
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


def sub(a, b):
    if b != 0:
        logging.debug("a/b=" + str(a / b))
        return a / b
    logging.error("Divide by zero!")


print(sub(2, 3))
print(sub(2, 0))

