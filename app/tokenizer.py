"""
Tokenizes an input file
"""

def tokenize(file_name):
  """
  Processes the text into tokens and creates a dict of them.
  :param f_name: file meant to be opens and processed
  :return:
    -p_tokens: returns dict of tokens with their line number being the key
  """

  # Create an empty dict to add tokens into and a count for line number
  code_line = {}

  # Read in all lines into a list.
  with open(file_name, 'r') as file:
    all_lines = file.readlines()

  # Look through each line for the dict. Do not add blank lines to dict.
  # We can add in blank lines again if needed in other uses
  for line_num, line in enumerate(all_lines):
    # First, increment the line number

    # See if the line is empty, do not save empty lines to dict.
    if line == '\n':
      line_token = ['EMPTY LINE']

      # And add the list into the dictionary
      code_line[line_num] = line_token
      continue

    # Now, go through the line and split it on the whitespace and save to list
    line_token = line.splitlines()

    # add the whole line to the code_line dict
    code_line[line_num] = line_token

  # after going through all lines, return dictionary
  return code_line
