def tokenize(f_name):
    """
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
    code_line = {}
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
             line_token = ['EMPTY LINE']

             # And add the list into the dictionary
             code_token[line_num] = line_token
             code_line[line_num] = line_token
             continue

        # Now, go through the line and split it on the whitespace and save to list
        line_token = line.splitlines()

        # add the whole line to the code_line dict
        code_line[line_num] = line_token

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
    return code_line
