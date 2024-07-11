import random
import string
import uuid


def random_correct_name(length1: int, length2: int, name_type=None) -> str:
    """
    Generates correct name and surname
    Args:
        length1 (int): name length
        length2  (int): surname length
        name_type : Select only first and last name
    """
    letters = string.ascii_lowercase
    if name_type == 'first_name':
        correct_name = ''.join(random.choice(letters) for i in range(length1))
    elif name_type == 'last_name':
        correct_name = ''.join(random.choice(letters) for i in range(length2))
    else:
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


def generate_random_five_digit_number(add_digits: int = 1):
    return random.randint(10000 * add_digits, 99999 * add_digits)


def generate_random_number(length):
    if length < 1:
        raise ValueError("Length must be at least 1")
    first_digit = random.randint(1, 9)
    if length == 1:
        return str(first_digit)

    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(length - 1)])

    return str(first_digit) + remaining_digits


def generate_random_pan():
    """Generate a random PAN number (10 characters: 5 letters, 4 digits, 1 letter)."""
    pan = ''.join(random.choices(string.ascii_uppercase, k=5))
    pan += ''.join(random.choices(string.digits, k=4))
    pan += random.choice(string.ascii_uppercase)
    return pan


def calculate_checksum(gst):
    """Calculate the checksum digit for the GST number."""
    gst_without_checksum = gst[:-1]
    factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    total = 0

    for i, char in enumerate(gst_without_checksum):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - 55  # Convert A-Z to 10-35
        total += value * factors[i]

    checksum_value = total % 36
    if checksum_value < 10:
        checksum_char = str(checksum_value)
    else:
        checksum_char = chr(checksum_value + 55)  # Convert 10-35 to A-Z

    return checksum_char


def generate_random_gst():
    """Generate a random GST number."""
    state_code = str(random.randint(1, 35)).zfill(2)  # State code (01-35)
    pan = generate_random_pan()  # Random PAN
    entity_code = str(random.randint(1, 9))  # Entity code
    default_z = 'Z'
    gst_without_checksum = state_code + pan + entity_code + default_z
    checksum = calculate_checksum(gst_without_checksum + '0')  # Calculate checksum
    gst = gst_without_checksum + checksum
    return gst

