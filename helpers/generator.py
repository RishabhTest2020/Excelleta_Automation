import random
import string
import uuid
from web_driver.config import short_date


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


def random_promo_email_generator() -> str:
    """
    Generates proper Promo e-mail with alias for testing purposes
    Returns (str): e-mail
    """
    ram_email = 'promo.test.automation+new' + uuid.uuid4().hex[:5] + '@gmail.com'
    return ram_email


def random_pricing_email_generator() -> str:
    """
    Generates proper Promo e-mail with alias for pricing purposes
    Returns (str): e-mail
    """
    date = short_date()
    ram_email = 'pricing+' + uuid.uuid4().hex[:4] + date + '@promo.com'
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
