import sys
import pickle


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