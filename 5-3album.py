from tkinter import *
from time import *

fnameList = ['딕셔너리푸드.png', '문자열뒤집기.png', '문자열쓰는거북이.png',
             '선형검색1.png', '선형검색2.png', '선형검색3.png', '이분탐색.png',
             '중심거북이.png', '해시테이블.png']
photoList = [None] * 9
num = 0

def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file=fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo


if __name__ == "__main__" :
    window = Tk()
    window.geometry("990x540")
    window.title("사진 앨범")

    photo = PhotoImage(file=fnameList[0])
    pLabel = Label(window, image=photo)

    btnPrev = Button(window, text = "<< 이전", command = clickPrev)
    btnNext = Button(window, text = "다음 >>", command = clickNext)

    btnPrev.place(x = 395, y = 10)
    btnNext.place(x = 595, y = 10)
    pLabel.place(x = 0, y = 50)

    window.mainloop()
