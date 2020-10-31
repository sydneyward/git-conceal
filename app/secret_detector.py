"""
Detects secrets in a given dictionary (pickled)
"""
import sys
import pickle
# import re
import myconstants # pylint: disable=import-error


def get_secret_dict(dictionary):
  """
  :return:
  :param dictionary::return: dict with line number - error key pair
  """
  secret_dict = []  # this should create empty dict for secrets

  for dict_key, dict_list in dictionary.items():
    secrets_list = []

    for item in dict_list:
      # use regex (constants) and high entropy to look for secrets
      if item in myconstants.CONCEAL_LIST:
        # found a secret! add it to the secrets list
        secrets_list.append(item)

    # after all secrets in that line found, add that line of secrets to secret_dict
    secret_dict[dict_key] = [secrets_list]

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
  print(len(code_lines))

  # get a dictionary of the list of secrets
  secret_list = get_secret_dict(code_lines)
