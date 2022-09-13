import string
from time import sleep
import random
import sys


# def rnd(strlen):
#     return(random.randint(0, strlen))


# stroka = 'Hello World!'
# strings = string.printable[:-38]
# strlen = len(strings) - 1

# ch = ''
# full = []
# for ch_stroka in stroka:
#     full.append(ch)
#     while ch_stroka != ch:
#         if ch_stroka in string:
#             ch = strings[rnd(strlen)]
#             # print(ch, sep=' ', end='', flush=True)
#             sleep(random.random() / 4)
#             sys.stdout.write('\r' + ''.join(full) + ch)
#             sys.stdout.flush()
#         else:
#             ch = ch_stroka


def string_print(string_line):
    return_line = []
    # strings = string.printable[:-38]
    # strlen = len(strings) - 1
    for char in string_line:
        return_line.append(char)
        sys.stdout.write(''.join(return_line) + '\r')
        sys.stdout.flush()
        sleep(random.randint(1, 5) / 25)
    sys.stdout.write('\n')


def char_select_print(string_line):
    print(string_line)
    strings = string.printable[-36:-6]
    full = []
    for ch in string_line:
        for i in range(1, random.randint(2, 5)):
            rand_char = strings[random.randint(0, len(strings) - 1)]
            sys.stdout.write('\r' + ''.join(full) + rand_char)
            sys.stdout.flush()
            sleep(random.randint(1, 3) / 15)
        full.append(ch)
        sys.stdout.write('\r' + ''.join(full))
        sys.stdout.flush()


def char_print(string_line):
    for ch in string_line:
        print(ch, sep=' ', end='', flush=True)
        sleep(random.random() / 10)


char_select_print("The quick brown fox jumps over the lazy dog")
