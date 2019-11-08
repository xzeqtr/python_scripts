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
    strings = list(string.printable[10:-38])
    # strlen = len(strings) - 1
    full = []
    for ch in string_line:
        strings = list(string.printable[10:-38])
        rand_char = ''
        if ch in strings:
            while rand_char != ch:
                rand_char = strings.pop(random.randint(0, len(strings) - 1))
                sleep(random.randint(1, 3) / 20)
                sys.stdout.write('\r' + ''.join(full) + rand_char)
                sys.stdout.flush()
            full.append(rand_char)
        else:
            full.append(ch)


def char_print(string_line):
    for ch in string_line:
        print(ch, sep=' ', end='', flush=True)
        sleep(random.random() / 10)


char_select_print("sdrgs er gsrt rtGRTG rTG sr er gsrt rtGRTG r gsrt rtGRTG rTG k\
    er gsrt rtGRTG rTG er gsrr gsrt rtGRTG rTG er gsrt rtGRTG rTG er gsrr \
    gsrt rtGRTG rTG er gsrt rtGRTG rTG er gsrr gsrt rtGRTG rTG er gsrt rtG\
    TG rTG er gsrrTG er gsrt rtGRTG rTG er gsrt rtGRTG rTG er gsrt rtGRTGr\
    TG er gsrt rtGRTG rTGTr")
