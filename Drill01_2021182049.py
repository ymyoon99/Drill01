import turtle

def key_w():
    turtle.setheading(90) #상
    turtle.forward(50)
    turtle.stamp()

def key_a():
    turtle.setheading(180) #좌
    turtle.forward(50)
    turtle.stamp()

def key_s():
    turtle.setheading(-90) #하
    turtle.forward(50)
    turtle.stamp()

def key_d():
    turtle.setheading(0) #우
    turtle.forward(50)
    turtle.stamp()

def restart(): #ESC
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(key_w,'w')
turtle.onkey(key_a,'a')
turtle.onkey(key_s,'s')
turtle.onkey(key_d,'d')
turtle.onkey(key_w,'W')
turtle.onkey(key_a,'A')
turtle.onkey(key_s,'S')
turtle.onkey(key_d,'D')
turtle.onkey(restart,'Escape')
turtle.listen()

turtle.exitonclick()


