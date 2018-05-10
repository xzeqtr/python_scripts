def update_progress(progress):
    print('\r[{0}] {1}%'.format('#'*(progress//10), progress))

update_progress(34)

import time, sys

k = 3210

for i in range(k):
    time.sleep(0.01)
    n = i * 100 // k
    sys.stdout.write('\r[{0}{1}] {2}%  {3} of {4}'.format('#'*(n//4), '%'*(25-n//4), n, i, k))
    # sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()

input("\r\nDone! Press Enter to exit...")