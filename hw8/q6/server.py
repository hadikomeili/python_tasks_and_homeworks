
import socket
import translators


def text_translate(func):
    def inner_func(*args, **kwargs):
        text = func(*args, **kwargs)
        x = translators.google(text, to_language='en')
        return x

    return inner_func


@text_translate
def get_text(text: str):
    return text


s = socket.socket()
port = 8000
ip = '0.0.0.0'
s.bind((ip, port))
s.listen()
c, addr = s.accept()
print('Translator is ready...')
while True:
    message = c.recv(2048).decode()
    res = get_text(message)
    c.send(res.encode())
