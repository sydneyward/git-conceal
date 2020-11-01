"""
Detects secrets in a given dictionary (pickled)
"""
import sys
import pickle
import re
import myconstants  # pylint: disable=import-error


def get_secret_dict(dictionary):
  """
  :return:
  :param dictionary::return: dict with line number - error key pair
  """
  secret_dict = []  # this should create empty dict for secrets

  #regex_matches = 

  for dict_key, dict_list in dictionary.items():  # pylint: disable=unused-variable
    secrets_list = []
    
    
    for item in dict_list:
      # use regex (constants) and high entropy to look for secrets
      #found_item = myconstants.FOLLOWED_BY_COLON_REGEX.match(item)
      found_secret = (
      myconstants.COLON_EQUALS_REGEX.match(item) or 
      myconstants.FOLLOWED_BY_COLON_REGEX.match(item) or 
      myconstants.FOLLOWED_BY_COLON_QUOTES_REQUIRED_REGEX.match(item) or 
      myconstants.FOLLOWED_BY_EQUAL_SIGNS_OPTIONAL_BRACKETS_OPTIONAL_AT_SIGN_QUOTES_REQUIRED_REGEX.match(item) or
      myconstants.FOLLOWED_BY_EQUAL_SIGNS_REGEX.match(item) or 
      myconstants.FOLLOWED_BY_EQUAL_SIGNS_QUOTES_REQUIRED_REGEX.match(item) or
      myconstants.FOLLOWED_BY_QUOTES_AND_SEMICOLON_REGEX.match(item)
      )
      
      #print(item)
      #print(found_item)
      if item in myconstants.CONCEAL_LIST or found_secret != None:
        #if item in myconstants.CONCEAL_LIST or item in myconstants.CONCEAL_LIST_REGEX: # didn't change anything
        # found a secret! add it to the secrets list
        secrets_list.append(item)

    # after all secrets in that line found, add that line of secrets to secret_dict
    secret_dict.append(secrets_list)

  return secret_dict


# Start up the program.
if __name__ == '__main__':

  # pickle name of the dictionary being used is passed in as a sys parameter
  # we can then extract the dictionary

  # Check that the file name is provided by sys arg.
  if len(sys.argv) < 2:
    print('Error: No pickle provided.')
    sys.exit(1)

  # Extract pickle name from sys arg.
  pickle_name = sys.argv[1]

  code_lines = pickle.load(open(pickle_name, 'rb'))

  # output to see what you're working with
  print(code_lines)   

  # this line of code will show you how many lines you have to shift through
  # just so you know, this can be removed after
  print("Number of lines in code file: " + str(len(code_lines)))

  # get a dictionary of the list of secrets
  secret_list = get_secret_dict(code_lines)

  # print list of secrets
  print(secret_list)
