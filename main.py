import secrets
import string


def generate(pwd_length: int):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(pwd_length))
    return password


def driver():
    pwd = generate(20)
    print(pwd)


driver()
