import sys

from utilities import prompt_for_input


def main(args):
    """

    :param args:
    :return:
    """
    # Write your program here
    name = prompt_for_input('Enter your name: ')
    print('Your name is {0}, right?'.format(repr(name)))


# If this is the main module, i.e. running as an entry to a program, then execute the main() function. Otherwise
# don't need to do anything.
if __name__ == "__main__":
    main(sys.argv[1:])