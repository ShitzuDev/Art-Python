from turtle import *
import colorsys
bgcolor('black')
tracer(2)
h=0.7
goto(150, 300)
for i in range(11000):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    begin_fill()
    circle(-50,60)
    forward(10-i*0.1)
    left(50)
    end_fill()
    h+=1/37
done()