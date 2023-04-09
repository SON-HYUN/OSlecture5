import turtleWritingChars as twc
import turtle

inStr = ''
sWidth, sHeight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

turtle.title('모듈을 활용한 거북이 글자 쓰기')
turtle.shape('turtle')
turtle.setup(width = sWidth + 50, height = sHeight + 50)
turtle.screensize(sWidth, sHeight)
turtle.screensize(sWidth, sHeight)
turtle.penup()
turtle.speed(500)

inStr = twc.getString()

for ch in inStr :
    tX, tY, tAngle, txtSize = twc.getXYAS(sWidth, sHeight)
    r, g, b = twc.getRGB()

    turtle.goto(tX, tY)
    turtle.left(tAngle)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font = ('맑은고딕', txtSize, 'bold'))

turtle.done()
