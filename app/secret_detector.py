"""
Detects secrets in a given dictionary (pickled)
"""
import math
import sys
import myconstants # pylint: disable=import-error
from tokenizer import tokenize # pylint: disable=import-error


def regex_match(code_lines):
  """ Some aspects borrowed from Yelp/detect-secrets
  :return:
  :param code_lines::return: dict with line number - error key pair
  """
  secret_dict = []  # this should create empty dict for secrets

  for line_num, code_line in code_lines.items():  # pylint: disable=unused-variable
    secrets_list = []

    for item in code_line:
    # use regex (constants) and high entropy to look for secrets
      # found_item = myconstants.FOLLOWED_BY_COLON_REGEX.match(item)
      found_secret = (
          myconstants.COLON_EQUALS_REGEX.search(item) or
          myconstants.FOLLOWED_BY_COLON_REGEX.search(item) or
          myconstants.FOLLOWED_BY_COLON_QUOTES_REQUIRED_REGEX.search(item) or
          myconstants.FOLLOWED_BY_EQUAL_SIGNS_OPTIONAL_BRACKETS_OPTIONAL_AT_SIGN_QUOTES_REQUIRED_REGEX.search(item) or
          myconstants.FOLLOWED_BY_EQUAL_SIGNS_REGEX.search(item) or
          myconstants.FOLLOWED_BY_EQUAL_SIGNS_QUOTES_REQUIRED_REGEX.search(item) or
          myconstants.FOLLOWED_BY_QUOTES_AND_SEMICOLON_REGEX.search(item)
      )

      if item in myconstants.CONCEAL_LIST or found_secret is not None:
        #if item in myconstants.CONCEAL_LIST or item in myconstants.CONCEAL_LIST_REGEX: # didn't change anything
        # found a secret! add it to the secrets list
        secrets_list.append(f"A regex was matched againsts: {item}")

    # after all secrets in that line found, add that line of secrets to secret_dict
    secret_dict.append(secrets_list)

  return secret_dict

def get_entropy_report(code_lines, secret_dict):
  """ This checks if the entropy check should be called and calls it.
      Input:
        code_lines(dict): contains the file being scanned parsed by lines
        secret_dict(dict): contains the secrets detected in the regex matcher
      Return:
        dict: where secrets were detected
  """
  characters_not_to_use = [',', '.', '(', ')', ';', ':', '"', '[', ']']
  for line_num, line in code_lines.items():
    if not secret_dict[line_num] and line[0] != "EMPTY LINE" and not any(x in line[0] for x in characters_not_to_use):
      tokens = line[0].split()
      for token in tokens:
        if len(token) > 7:
          entropy = entropy_check(token)
          if entropy > 3.3:
            secret_dict[line_num].append(f"Token: {token} returned a shannon entropy of {entropy}")
  return secret_dict

def entropy_check(token):
  """ This entropy checker was borrowed from
      https://towardsdatascience.com/the-intuition-behind-shannons-entropy-e74820fe9800
      Input:
        token(string): token to run the entropy on
      Return:
        float: entropy value
  """
  entropy = 0
  # 265 possible ASCII characters
  for char_x in range(256):
    prob_x = float(token.count(chr(char_x))/len(token))
    if prob_x > 0:
      entropy += - prob_x * math.log(prob_x, 2)
  return entropy

def main():
  """ The main function """
  proj_name = sys.argv[1]
  file_path = "files.txt"
  with open(file_path) as file:
    file_names = file.read().splitlines()
  for file_name in file_names:
    if file_name != "files.txt":
      count_secrets = 0
      code_lines = tokenize(f"{proj_name}/{file_name}")
      secret_list = regex_match(code_lines)
      secret_list = get_entropy_report(code_lines, secret_list)
      print(f"For file \'{file_name}\':")
      for line_num, item in enumerate(secret_list):
        if item:
          count_secrets += 1
          print(f"  line: {line_num}    {item[0]}")
      print(f"There were {count_secrets} secrets detected.\n\n")

if __name__ == '__main__':
  main()
