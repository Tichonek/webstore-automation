from config import DOMAINS, PASSWORD_CONFIG, YEAR_CONFIG
from faker import Faker
from unidecode import unidecode
import random
import json

faker = Faker('pl-PL')

def generateFirstName():
    firstName = faker.first_name()
    return firstName

def generateLastName():
    lastName = faker.last_name()
    return lastName

def generateEmail(firstName, lastName):
    domain = random.choice(DOMAINS)
    firstName = unidecode(firstName.lower())
    lastName = unidecode(lastName.lower())
    email = f'{firstName}.{lastName}{domain}'
    return email

def generatePassword():
    min_length = PASSWORD_CONFIG['min_length']
    max_length = PASSWORD_CONFIG['max_length']
    include_digits = PASSWORD_CONFIG['include_digits']
    include_specials = PASSWORD_CONFIG['include_specials']
    special_chars = PASSWORD_CONFIG['special_chars']
    chars_lower = PASSWORD_CONFIG['chars_lower']
    chars_upper = PASSWORD_CONFIG['chars_upper']
    digits = PASSWORD_CONFIG['digits']

    chars = []
    chars.extend(char for char in chars_lower)
    chars.extend(char for char in chars_upper)
    
    if include_digits:
        chars += digits
    
    if include_specials:
        chars += special_chars
    
    passwordLen = random.randint(min_length, max_length)
    passwordChars = []

    for char in range(passwordLen):
        char = random.choice(chars)
        passwordChars.append(char)
    
    random.shuffle(passwordChars)

    password = ''.join(passwordChars)

    return password

def isLeapYear(year):
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True

    return False

def generateBirthDate(config=None):
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
    filename = '../test_data.json'
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(person, f, indent=4, ensure_ascii=False)
        print('Person saved to file')
    except OSError as e:
        print(f'Save file error: {e}')
