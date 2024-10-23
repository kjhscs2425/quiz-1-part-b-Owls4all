import turtle
t= turtle
t.up()         #  |
t.goto(-50,50) #  |- I wanted it centered at 0,0
t.down()       #  |
for i in range(4):
    t.fd(100)
    t.rt(90)
t.fd(50)
t.rt(45)
for i in range(4):
    t.fd(71)
    t.rt(90)

turtle.exitonclick()