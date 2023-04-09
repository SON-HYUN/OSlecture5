import random
from tkinter.simpledialog import *

def getString() :
    retStr = ''
    retStr = askstring('문자열 입력', '거북이가 작성할 문자열을 입력')
    return retStr

def getRGB() :
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g ,b)

def getXYAS(sWidth, sHeight) :
    x, y, angle, size = 0, 0, 0, 0
    x = random.randrange(-sWidth / 2, sWidth / 2)
    y = random.randrange(-sHeight / 2, sHeight / 2)
    angle = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return [x, y, angle, size]