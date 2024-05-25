import random
import string
import uuid


def random_correct_name(length1: int, length2: int) -> str:
    """
    Generates correct name and surname
    Args:
        length1 (int): name length
        length2  (int): surname length
    """
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length1))
    surname = ''.join(random.choice(letters) for i in range(length2))
    correct_name = name + ' ' + surname
    return correct_name


def random_email_generator() -> str:
    """
    Generates proper Promo e-mail with alias for testing purposes
    Returns (str): e-mail
    """
    ram_email = 'testautom' + uuid.uuid4().hex[:5] + '@yopmail.com'
    return ram_email



def random_password_string(length: int) -> str:
    """
    Generates random password with chosen length
    Args:
        length (int): password length
    """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password


def generate_random_five_digit_number():
    return random.randint(10000, 99999)