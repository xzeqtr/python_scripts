import os
import multiprocessing
import subprocess
from platform import system as system_name # Returns the system/OS name

DNULL = open(os.devnull, 'w')
# devices = ['192.168.125.2', '192.168.100.155', '8.8.8.8', '4.4.4.4', '95.31.27.197']
devices = ['192.168.1.' + str(x) for x in range (2, 254)]


def ping(host, mp_queue):
    # Ping parameters as function of OS
    parameters = "-n" if system_name().lower()=="windows" else "-c"
    response = subprocess.call(["ping", parameters, "2", "-w", "200", host], stdout=DNULL)
    if response == 0:
        print(host, 'is up!')
        result = True
    else:
        #print(host, 'is down!')
        result = False
    mp_queue.put((result,host))

def worker(devices):
    mp_queue = multiprocessing.Queue()
    processes = []
    for device in devices:
        p = multiprocessing.Process(target=ping, args=(device, mp_queue))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    results = {True:[], False:[]}
    for p in processes:
        key, value =  mp_queue.get()
        results[key] += [value]
    return results[True], results[False]


if __name__ == '__main__':
    success, failed = worker(devices)
    input("Press Enter to continue...")