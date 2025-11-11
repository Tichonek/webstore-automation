from scripts.data_generators import *
from unittest.mock import patch
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