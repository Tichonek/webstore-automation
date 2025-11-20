from scripts.data_generators import *
from scripts.main import *
from unittest.mock import patch
from unittest.mock import mock_open, patch, call
import re
import pytest

def test_generateFirstName():
    firstName = generateFirstName()
    assert isinstance(firstName, str)
    assert len(firstName) > 0
    assert firstName[0].isupper()


def test_generateLastName():
    lastName = generateLastName()
    assert isinstance(lastName, str)
    assert len(lastName) > 0
    assert lastName[0].isupper()

def test_generateEmail():
    email = generateEmail('Jan', 'Kowalski')
    assert len(email) > 0
    assert '@' in email
    assert '.' in email
    assert email == email.lower()

def test_generateEmail_matches_pattern():
    email = generateEmail('Kamil', 'Wojciechowski')
    pattern = r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$"
    assert re.match(pattern, email)

def test_generateEmail_has_no_polish_characters():
    email = generateEmail('Łukasz', 'Żółć')
    for char in 'ąćęłńóśżź':
        assert char not in email

def test_generateEmail_uses_domain(monkeypatch):
    test_domain = '@example.com'
    monkeypatch.setattr(random, "choice", lambda _: test_domain)

    email = generateEmail('Filip', 'Kowalski')
    assert email.endswith(test_domain)

@pytest.mark.parametrize(
        'year, expected',
        [
            (2000, True),
            (1900, False),
            (2004, True),
            (2001, False),
            (2024, True),
            (2100, False),
        ]
)
def test_isLeapYear(year, expected):
    result = isLeapYear(year)
    assert result == expected

@pytest.fixture
def mock_year_config():
    return {
        'min_year': 2000,
        'max_year': 2000
    }

@patch('scripts.data_generators.random.randint')
def test_generateBirthDate_non_leap(mock_randint, mock_year_config):
    mock_randint.side_effect = [2001, 2, 15] #  year, month, day
    result = generateBirthDate(config=mock_year_config)

    assert result == '02/15/2001'
    assert mock_randint.call_count == 3

@patch('scripts.data_generators.random.randint')
def test_generateBirthDate_lepa_year(mock_randint, mock_year_config):
    mock_randint.side_effect = [2000, 2, 29]
    result = generateBirthDate(config=mock_year_config)

    assert result == '02/29/2000'
    assert mock_randint.call_count == 3

@pytest.fixture
def mock_password_config():
    return {
        'min_length': 8,
        'max_length': 8,
        'include_digits': True,
        'include_specials': True,
        'special_chars': '!@',
        'chars_lower': 'ab',
        'chars_upper': 'CD',
        'digits': '12'
    }
@patch('scripts.data_generators.random.randint')
@patch('scripts.data_generators.random.choice')
@patch('scripts.data_generators.random.shuffle')
def test_generatePassword_basic(mock_shuffle, mock_choice, mock_randint, mock_password_config):
    mock_randint.return_value = 8
    mock_choice.side_effect = list('abCD12!@')
    mock_shuffle.side_effect = lambda x: x

    result = generatePassword(config=mock_password_config)

    assert len(result) == 8
    assert set(result).issubset(set('abCD12!@'))
    assert result == 'abCD12!@'


def test_generatePassword_no_digits_or_specials(mock_password_config):
    mock_password_config['include_digits'] = False
    mock_password_config['include_specials'] = False

    with patch('scripts.data_generators.random.randint', return_value = 8), \
        patch('scripts.data_generators.random.choice', side_effect = list('abCDabCD')), \
        patch('scripts.data_generators.random.shuffle', lambda x: x):
        
        result = generatePassword(config=mock_password_config)
    
    assert set(result).issubset(set('abCD'))
    assert not any(c.isdigit() for c in result)
    assert all(c in 'abCD' for c in result)

def test_generatePassword_includes_specials_and_digits(mock_password_config):
    mock_password_config['include_digits'] = True
    mock_password_config['include_specials'] = True

    with patch('scripts.data_generators.random.randint', return_value = 8), \
        patch('scripts.data_generators.random.choice', side_effect = lambda seq: seq[0]), \
        patch('scripts.data_generators.random.shuffle', lambda x: x):

        result = generatePassword(config=mock_password_config)

    assert len(result) == 8
    allowed_chars = set('abcd12!@#$')
    assert set(result).issubset(allowed_chars)

@pytest.fixture
def sample_person_data():
    """Fixture zwracająca przykładowe dane osoby"""
    return {
        "firstName": "Jan",
        "lastName": "Kowalski",
        "email": "jan.kowalski@test.com",
        "password": "Secret123!",
        "birthDate": "12/31/1990"
    }
def test_generatePerson_returns_dict(sample_person_data):
    person = generatePerson(**sample_person_data)

    assert isinstance(person, dict)

def test_generatePerson_contains_all_keys(sample_person_data):
     person = generatePerson(**sample_person_data)
     for key, value in sample_person_data.items():
        assert person[key] == value

def test_generatePerson_values_match_arguments(sample_person_data):
    person = generatePerson(**sample_person_data)

    for key, value in person.items():
        assert person[key] == value

def test_saveToJSON_calls_open_json_dump(sample_person_data):
    m_open = mock_open()
    with patch('builtins.open', m_open), \
        patch('json.dump') as mock_json_dump, \
        patch('builtins.print') as mock_print:

        saveToJSON(sample_person_data)

        m_open.assert_called_once_with('../test_data.json', 'w', encoding='utf-8')

        mock_json_dump.assert_called_once_with(sample_person_data, m_open(), indent=4, ensure_ascii=False)

        mock_print.assert_called_once_with('Person saved to file')

def test_saveToJSON_handles_oserror(sample_person_data):
    with patch('builtins.open', side_effect=OSError('Disk full')), \
        patch('builtins.print') as mock_print:

        saveToJSON(sample_person_data)

        mock_print.assert_called_once()
        args = mock_print.call_args[0][0]
        assert 'Save file error' in args
        assert 'Disk full' in args

def test_main_integration(sample_person_data):
    with patch('scripts.main.generateFirstName', return_value=sample_person_data['firstName']), \
         patch('scripts.main.generateLastName', return_value=sample_person_data['lastName']), \
         patch('scripts.main.generateEmail', return_value=sample_person_data['email']), \
         patch('scripts.main.generatePassword', return_value=sample_person_data['password']), \
         patch('scripts.main.generateBirthDate', return_value=sample_person_data['birthDate']), \
         patch('scripts.main.generatePerson', return_value={}) as mock_person, \
         patch('scripts.main.saveToJSON') as mock_save:

        main()

        mock_person.assert_called_once_with(
            sample_person_data['firstName'],
            sample_person_data['lastName'],
            sample_person_data['email'],
            sample_person_data['password'],
            sample_person_data['birthDate'],
        )

        mock_save.assert_called_once_with({})
