import random
import time


def rand_mover():
    width, height = pyautogui.size()
    x_start = 100
    y_start = 50
    dist = 40
    pyautogui.moveTo(x_start, y_start)
    mul_x, mul_y = 1, 1
    x_old, y_old = x_start, y_start
    while 1:
        x_new = x_old + random.randint(10, 24) * mul_x
        y_new = y_old + random.randint(10, 24) * mul_y
        if x_new > width - dist:
            mul_x = -1
        if x_new < dist:
            mul_x = 1
        if y_new > height - dist:
            mul_y = -1
        if y_new < dist:
            mul_y = 1
        # pyautogui.moveRel(x_new, y_new)
        pyautogui.moveTo(x_new, y_new)
        x_old, y_old = x_new, y_new


def onepxmove():
    mul_x = 1
    while 1:
        mul_x = mul_x * (-1)
        cur_x, cur_y = pyautogui.position()
        pyautogui.moveTo(cur_x + mul_x, cur_y)
        time.sleep(1)


# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

if __name__ == "__main__":
    try:
        import pyautogui
    except:
            import subprocess, sys
            print('installing pyautogui...')
            subprocess.check_output([sys.executable, '-m', 'pip', 'install', 'pyautogui'])
            import pyautogui
    onepxmove()
