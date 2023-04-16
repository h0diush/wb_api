import random

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify(password, hash)


def generate_code() -> str:
    random_num = random.randrange(100000000, 999999999)
    return str(random_num)
