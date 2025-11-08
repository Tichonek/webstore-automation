from scripts.data_generators import *
import re

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
    email = generateEmail('Jan', 'KowaLski')
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

