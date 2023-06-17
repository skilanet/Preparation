from turtle import *

tracer(0)
screensize(500, 500)
r = 40

lt(90)
for i in range(7):
    fd(10 * r)
    rt(120)

up()

for x in range(-50, 51):
    for y in range(-50, 51):
        goto(x * r, y * r)
        dot(3, 'green')

update()
exitonclick()
