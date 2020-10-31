"""
Tokenizes a file and creates a dict of said tokens
"""

import sys
import pickle


def tokenize(f_name):
  """
  :return:
  Processes the text into tokens and creates a dict of them.
  :param f_name: file meant to be opens and processed
  :return:
    -p_tokens: returns dict of tokens with their line number being the key
  """
  print('Input file:', f_name)

  # Open the file.
  input_file = open('%s' % f_name, 'r')

  # Create an empty dict to add tokens into and a count for line number
  code_token = {}
  line_num = 0

  # Read in all lines into a list.
  all_lines = input_file.readlines()

  # For debugging purposes.
  print(all_lines)

  # Look through each line for the dict. Do not add blank lines to dict.
  # We can add in blank lines again if needed in other uses
  for line in all_lines:
    # First, increment the line number
    line_num += 1

    # See if the line is empty, do not save empty lines to dict.
    if line == '\n':
      continue

    # Now, go through the line and split it on the whitespace and save to list
    line_token = line.split()

    # Last word in the list may have an end of line deliminator, remove him!
    last_index = len(line_token) - 1
    last_item = line_token.pop(last_index)

    if last_item.endswith(';') or last_item.endswith('.'):
      last_item = last_item[:-1]

    # add item back to list
    line_token.append(last_item)

    # And add the list into the dictionary
    code_token[line_num] = line_token

  # after going through all lines, return dictionary
  return code_token


# Start up the program.
if __name__ == '__main__':

  # Check that the file name is provided by sys arg.
  if len(sys.argv) < 2:
    print('Error: No file provided to check.')
    sys.exit(1)

  # Extract file name from sys arg.  This may need to change.
  # This can also be altered to filter through several files if needed.
  filename = sys.argv[1]

  # Tokenize raw text by passing file name(and preprocess). I think this will be useful but it
  # can be easily removed if capital letters or anything help with high entropy calculations
  token_dict = tokenize(filename)

  # Print for debugging
  print(token_dict)

  # Remove .txt or whatnot from filename
  base_file = filename.split('.')

  # Pickle the file so it can be used by other programs, based off filename
  filename_pickle = base_file[0] + '.pickle'

  pickle.dump(token_dict, open(filename_pickle, 'wb'))
