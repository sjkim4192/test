
import pyautogui as pag
import keyboard
import time
from PIL import Image
#import opencv2

file_num=0
#while True:
print('set position(press q)')
while True:
    if keyboard.is_pressed("q"):
            start = pag.position()
            time.sleep(0.2)
            break
while True:
    if keyboard.is_pressed("q"):
        end = pag.position()
        time.sleep(0.2)
        break

xx = start[0]
yy = start[1]
ww = end[0] - start[0]
hh = end[1] - start[1]

print('set drag area(press d)')
while True:
    if keyboard.is_pressed("d"):
        s_drag = pag.position()
        time.sleep(0.2)
        break
while True:
    if keyboard.is_pressed("d"):
        e_drag = pag.position()
        time.sleep(0.2)
        break
drag_x = s_drag[0]-e_drag[0]
drag_y = s_drag[1]-e_drag[1]
filepath = 'C:/Users/SJKIM/Desktop/ddd/photo/'
while True:
    image = pag.screenshot(filepath+str(file_num)+'.png', region = (xx,yy,ww,hh))
    #image = Image.open(filepath)
        
    pag.drag(drag_x,drag_y,mouseDownUp=0)
    file_num += 1
    time.sleep(1)
    #if keyboard.is_pressed("k"):
    #    break