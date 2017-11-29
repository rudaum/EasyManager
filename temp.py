from subprocess import Popen, PIPE
from openpyxl import Workbook
from openpyxl.styles import Border, Side, PatternFill, Font
from collections import OrderedDict
import getopt
from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))