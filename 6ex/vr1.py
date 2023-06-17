from turtle import *

tracer(0)
screensize(2000, 2000)
r = 80

lt(90)
for i in range(4):
    color('purple')
    fd(9 * r)
    rt(90)

for i in range(3):
    color('cyan')
    fd(9 * r)
    rt(120)

up()

for x in range(-50, 51):
    for y in range(-50, 51):
        goto(x * r, y * r)
        dot(3, 'green')

update()
exitonclick()
