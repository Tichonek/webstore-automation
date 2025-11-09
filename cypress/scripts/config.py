DOMAINS = ['@example.com', '@test.pl', '@wp.pl', '@mail.net', '@gmail.com']

PASSWORD_CONFIG = {
    'min_length': 8,
    'max_length': 12,
    'include_digits': True,
    'include_specials': True,
    'special_chars': '!@#$%^&*()',
    'chars_lower': 'abcdefghijklmnopqrstuvwxyz',
    'chars_upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'digits': '0123456789'
}

YEAR_CONFIG = {
    'min_year': 1960,
    'max_year': 2010
}