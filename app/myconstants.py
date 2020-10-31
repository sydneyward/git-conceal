"""
Constants for use in secret_detector.py
"""
import re


# list of keywords to look for secrets
CONCEAL_LIST = ['AKIA',
                'apikey',
                'api_key',
                'aws_secret_access_key',
                'BEGIN DSA PRIVATE KEY',
                'BEGIN EC PRIVATE KEY',
                'BEGIN OPENSSH PRIVATE KEY',
                'BEGIN PGP PRIVATE KEY BLOCK',
                'BEGIN PRIVATE KEY',
                'BEGIN RSA PRIVATE KEY',
                'BEGIN SSH2 ENCRYPTED PRIVATE KEY',
                'db_pass',
                'password',
                'passwd',
                'pw',
                'private_key',
                'secret']

# here, we define some regexes that will help us with different configurations
# that a keyword/secret pair might show up in - props to detect-secrets
CONCEAL_LIST_REGEX = r'|'.join(CONCEAL_LIST)
SECRET = r'[^\s]+'
CLOSE = r'[]\'"]{0,2}'
WHITESPACE = r'\s*?'
NONWHITESPACE = r'[^/s]*?'
QUOTATION_MARK = r'[\'"]'
SQUARE_BRACKETS = r'(\[\])'

COLON_EQUALS_REGEX = re.compile(
    # e.g. my_password := "secretpass" or my_password := secretpass
    r'({list})({closing})?{space}:=?{space}({quote}?)({oops})(\3)'.format(
        list=CONCEAL_LIST_REGEX,
        closing=CLOSE,
        quote=QUOTATION_MARK,
        space=WHITESPACE,
        oops=SECRET,
    ),
)

FOLLOWED_BY_COLON_REGEX = re.compile(
    # e.g. api_key: foo
    r'({list})({closing})?:{space}({quote}?)({oops})(\3)'.format(
        list=CONCEAL_LIST_REGEX,
        closing=CLOSE,
        quote=QUOTATION_MARK,
        space=WHITESPACE,
        oops=SECRET,
    ),
)

FOLLOWED_BY_COLON_QUOTES_REQUIRED_REGEX = re.compile(
    # e.g. api_key: "foo"
    r'({list})({closing})?:({space})({quote})({oops})(\4)'.format(
        list=CONCEAL_LIST_REGEX,
        closing=CLOSE,
        quote=QUOTATION_MARK,
        space=WHITESPACE,
        oops=SECRET,
    ),
)

FOLLOWED_BY_EQUAL_SIGNS_OPTIONAL_BRACKETS_OPTIONAL_AT_SIGN_QUOTES_REQUIRED_REGEX = re.compile(
    # e.g. my_password = "secretpass"
    # e.g. my_password = @"secretpass"
    # e.g. my_password[] = "secretpass";
    r'({list})({brackets})?{space}={space}(@)?(")({oops})(\5)'.format(  # noqa: E501
        list=CONCEAL_LIST_REGEX,
        brackets=SQUARE_BRACKETS,
        space=WHITESPACE,
        oops=SECRET,
    ),
)

FOLLOWED_BY_EQUAL_SIGNS_REGEX = re.compile(
    # e.g. my_password = secretpass
    r'({list})({closing})?{space}={space}({quote}?)({oops})(\3)'.format(
        list=CONCEAL_LIST_REGEX,
        closing=CLOSE,
        quote=QUOTATION_MARK,
        space=WHITESPACE,
        oops=SECRET,
    ),
)

FOLLOWED_BY_EQUAL_SIGNS_QUOTES_REQUIRED_REGEX = re.compile(
    # e.g. my_password = "secretpass"
    r'({list})({closing})?{space}={space}({quote})({oops})(\3)'.format(
        list=CONCEAL_LIST_REGEX,
        closing=CLOSE,
        quote=QUOTATION_MARK,
        space=WHITESPACE,
        oops=SECRET,
    ),
)

FOLLOWED_BY_QUOTES_AND_SEMICOLON_REGEX = re.compile(
    # e.g. private_key "something";
    r'({list}){non_whitespace}{space}({quote})({oops})(\2);'.format(
        list=CONCEAL_LIST_REGEX,
        non_whitespace=NONWHITESPACE,
        space=WHITESPACE,
        quote=QUOTATION_MARK,
        oops=SECRET,
    ),
)
