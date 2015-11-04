import re
import sys

_newline_pattern = re.compile('^([^\n]+)\n')


def prompt_for_input(prompt):
    """Prompt the user for some input.

    This reads in an entire line, i.e. the user must press enter when finish entering the data. The 'enter' or newline
    character will be stripped out of the returned value.

    :param prompt: The prompt to be displayed to the user.
    :type prompt: str
    :return: The string entered by the user (minus any newline)
    :rtype: str
    """
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ret = sys.stdin.readline()

    # Now strip out the newline character(s) at the end.
    match = _newline_pattern.match(ret)
    if match:
        # Found the newline pattern, return the stripped out srting
        return match.group(1)

    # No newline found, juswt return the string as is.
    return