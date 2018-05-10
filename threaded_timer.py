import threading
import time
 
 
stop_c = False
 
def c(n):
    ti = n
    while not stop_c:
        time.sleep(1)
        ti -= 1
        print('осталось', ti, 'секунд')
        
        if ti == 0:
            print('Время вышло!')
            ti = n
        else:
            continue
 
 
def ans(ans):
    global stop_c
    ans = input()
    if ans == '10':
        print(' верно ')
    else:
        print(' неверно ')
    stop_c = True
 
 
o = threading.Thread(target=ans, args=(1, ))
t = threading.Thread(target=c, args=(15, ))
print('сколько будет 5 + 5?')
print('у вас есть 15 секунд')
o.start()
t.start()