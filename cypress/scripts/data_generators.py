from config import DOMAINS, PASSWORD_CONFIG, YEAR_CONFIG
from faker import Faker
from unidecode import unidecode
import random
import json

faker = Faker('pl-PL')

def generateFirstName():
    """
    Generate a random first name

    Returns:
        str: A randomly generated first name
    """

    firstName = faker.first_name()
    return firstName

def generateLastName():
    """
    Generate a random last name

    Returns:
        str: A randomly generated last name
    """

    lastName = faker.last_name()
    return lastName

def generateEmail(firstName, lastName):
    """
    Generate an email address based on a first and last name

    The function normalizes the provided names, 
    randomly selects a domain from the DOMAINS list, 
    and constructs an email in the format: firstName.lastName@domain

    Args:
        firstName (str): The person's first name
        lastName (str): Tje person's last name

    Returns:
        str: A generated email address using the provided names and random domain
    """

    domain = random.choice(DOMAINS)
    firstName = unidecode(firstName.lower())
    lastName = unidecode(lastName.lower())
    email = f'{firstName}.{lastName}{domain}'
    return email

def generatePassword(config=None):
    """
    Generate a random password based on a configuration dictionary.

    The function constructs a password consisting of lowercase letters,
    uppercase letters, and optionally digits or special characters.
    Behavior can be customized through a configuration dictionary. If no
    configuration is provided, the default `PASSWORD_CONFIG` is used.

    The configuration dictionary supports the following keys:
        - min_length (int): Minimum password length.
        - max_length (int): Maximum password length.
        - include_digits (bool): Whether to include numeric characters.
        - include_specials (bool): Whether to include special characters.
        - special_chars (str): A string of allowed special characters.
        - chars_lower (str): Allowed lowercase characters.
        - chars_upper (str): Allowed uppercase characters.
        - digits (str): Allowed digit characters.

    Args:
        config (dict, optional): Configuration for password generation.
            Defaults to `PASSWORD_CONFIG`.

    Returns:
        str: A randomly generated password that meets the configuration criteria.
    """

    if config is None:
        config = PASSWORD_CONFIG

    min_length = config['min_length']
    max_length = config['max_length']
    include_digits = config['include_digits']
    include_specials = config['include_specials']
    special_chars = config['special_chars']
    chars_lower = config['chars_lower']
    chars_upper = config['chars_upper']
    digits = config['digits']

    chars = list(chars_lower + chars_upper)
    
    if include_digits:
        chars += list(digits)
    
    if include_specials:
        chars += list(special_chars)
    
    passwordLen = random.randint(min_length, max_length)
    passwordChars = []

    for char in range(passwordLen):
        char = random.choice(chars)
        passwordChars.append(char)
    
    random.shuffle(passwordChars)

    password = ''.join(passwordChars)

    return password

def isLeapYear(year):
    """
    Determine whether a given year is a leap year.

    A year is considered a leap year if it meets the following conditions:
    - It is divisible by 400, or
    - It is divisible by 4 but not by 100.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, otherwise False.
    """

    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True

    return False

def generateBirthDate(config=None):
    """
    Generate a random birth date based on a configuration dictionary.

    The function selects a random year within the configured range, then
    randomly generates a valid month and day. For February, it correctly
    accounts for leap years using the `isLeapYear` function.

    The configuration dictionary supports the following keys:
        - min_year (int): Minimum year that can be generated.
        - max_year (int): Maximum year that can be generated.

    The returned date is formatted as ``MM/DD/YYYY``.

    Args:
        config (dict, optional): Configuration specifying the year range.
            Defaults to ``YEAR_CONFIG``.

    Returns:
        str: A randomly generated birth date in ``MM/DD/YYYY`` format.
    """

    if config is None:
        config = YEAR_CONFIG

    min_year = config['min_year']
    max_year = config['max_year']

    year = random.randint(min_year, max_year)
    month = random.randint(1,12)

    
    if month in (1, 3, 5, 7, 8, 10, 12):
        daysInMonth = random.randint(1, 31)
    elif month in (4, 6, 9, 11):
        daysInMonth = random.randint(1, 30)
    elif month == 2:
        if isLeapYear(year):
            daysInMonth = 29
        else:
            daysInMonth = 28

    day = random.randint(1,daysInMonth)
    
    birthDate = f'{month:02d}/{day:02d}/{year}'
    return birthDate

def generatePerson(firstName, lastName, email, password, birthDate):
    """
    Create a dictionary representing a person's generated data.

    This function aggregates previously generated user data—such as
    first name, last name, email, password, and birth date into a single
    structured dictionary. It also prints a summary of the generated data
    for debugging or logging purposes.

    Args:
        firstName (str): The person's first name.
        lastName (str): The person's last name.
        email (str): The person's email address.
        password (str): The generated password.
        birthDate (str): The generated birth date in ``MM/DD/YYYY`` format.

    Returns:
        dict: A dictionary containing the person's generated data with keys:
            ``firstName``, ``lastName``, ``email``, ``password``, ``birthDate``.
    """

    person = {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'password': password,
        'birthDate': birthDate
    }

    result = [firstName, lastName, email, password, birthDate]
    print(f'Generated data: {result}')
    return person

def saveToJSON(person):
    """
    Save a person's data to a JSON file.

    The function writes the provided `person` dictionary to a JSON file
    located at '../test_data.json'. It formats the JSON with an indentation
    of 4 spaces and ensures non-ASCII characters are preserved.

    Args:
        person (dict): The dictionary containing a person's generated data.

    Returns:
        None

    Notes:
        If the file cannot be saved due to an OS error, the function will
        print an error message.
    """
    
    filename = '../test_data.json'
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(person, f, indent=4, ensure_ascii=False)
        print('Person saved to file')
    except OSError as e:
        print(f'Save file error: {e}')
