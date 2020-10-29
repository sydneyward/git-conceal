import sys
import pickle
import re


# Start up the program.
if __name__ == '__main__':

    # pickle name of the dictionary being used is passed in as a sys parameter
    # we can then extract the dictionary

    # Check that the file name is provided by sys arg.
    if len(sys.argv) < 2:
      print('Error: No pickle provided.')
      quit()

    # Extract pickle name from sys arg.
    pickle_name = sys.argv[1]

    code_lines = pickle.load(open(pickle_name, 'rb'))

    # output to see what you're working with
    print(code_lines)

    # this line of code will show you how many lines you have to shift through
    # just so you know, this can be removed after
    print(len(code_lines))
    
    # list of keywords to look for secrets
    concealList = (
      'AKIA'
      'apikey',
      'api_key',
      'aws_secret_access_key',
      'BEGIN DSA PRIVATE KEY'
      'BEGIN EC PRIVATE KEY'
      'BEGIN OPENSSH PRIVATE KEY'
      'BEGIN PGP PRIVATE KEY BLOCK'
      'BEGIN PRIVATE KEY'
      'BEGIN RSA PRIVATE KEY'
      'BEGIN SSH2 ENCRYPTED PRIVATE KEY'
      'db_pass',
      'password',
      'passwd',
      'pw'
      'private_key',
      'secret',
   )
   
   # here, we define some regexes that will help us with different configurations
   # that a keyword/secret pair might show up in - props to detect-secrets
   concealListRegex = r'|'.join(concealList)
   secret = r'[^\s]+'
   
   close = r'[]\'"]{0,2}'
   whitespace = r'\s*?'
   nonWhitespace = r'[^/s]*?'
   quotationMark = r'[\'"]'
   squareBrackets = r'(\[\])'
   
   colonEqualsRegex = re.compile(
   # e.g. my_password := "bar" or my_password := bar
      r'({list})({closing})?{whitespace}:=?{space}({quote}?)({oops})(\3)'.format(
         list = concealListRegex,
         closing = close,
         quote = quotationMark,
         space = whitespace,
         oops = secret,
      ),
   )
   
   FOLLOWED_BY_COLON_REGEX = re.compile(
   # e.g. api_key: foo
      r'({list})({closing})?:{space}({quote}?)({oops})(\3)'.format(
         list = concealListRegex,
         closing = close,
         quote = quotationMark,
         space = whitespace,
         oops = secret,
      ),
   )
   
   FOLLOWED_BY_COLON_QUOTES_REQUIRED_REGEX = re.compile(
   # e.g. api_key: "foo"
      r'({list})({closing})?:({space})({quote})({oops})(\4)'.format(
         list = concealListRegex,
         closing = close,
         quote = quotationMark,
         whitespace = whitespace,
         oops = secret,
      ),
   )
   
   FOLLOWED_BY_EQUAL_SIGNS_OPTIONAL_BRACKETS_OPTIONAL_AT_SIGN_QUOTES_REQUIRED_REGEX = re.compile(
   # e.g. my_password = "bar"
   # e.g. my_password = @"bar"
   # e.g. my_password[] = "bar";
      r'({list})({brackets})?{space}={space}(@)?(")({oops})(\5)'.format(   # noqa: E501
         list = concealListRegex,
         brackets = squareBrackets,
         space = whitespace,
         oops = secret,
      ),
   )
   
   FOLLOWED_BY_EQUAL_SIGNS_REGEX = re.compile(
   # e.g. my_password = bar
      r'({list})({closing})?{space}={space}({quote}?)({oops})(\3)'.format(
         list = concealListRegex,
         closing = close,
         quote = quotationMark,
         space = whitespace,
         oops = secret,
      ),
   )
   
   FOLLOWED_BY_EQUAL_SIGNS_QUOTES_REQUIRED_REGEX = re.compile(
   # e.g. my_password = "bar"
      r'({list})({closing})?{space}={space}({quote})({oops})(\3)'.format(
         list = concealListRegex,
         closing = close,
         quote = quotationMark,
         space = whitespace,
         oops = secret,
      ),
   )
   
   FOLLOWED_BY_QUOTES_AND_SEMICOLON_REGEX = re.compile(
   # e.g. private_key "something";
      r'({list}){non_whitespace}{space}({quote})({oops})(\2);'.format(
         list = concealList,
         non_whitespace = nonWhitespace,
         space = whitespace,
         quote = quotationMark,
         oops = secret,
      ),
   )
   
   
