# Simple "Etch-a-Sketch" program created by Alexander Peng on 2024/08/04. This program uses Screen's listen()
# method to incorporate user input into Python graphics.


from turtle import Turtle, Screen


def move_forwards():
    t.forward(1)


def move_backwards():
    t.backward(1)


def turn_left():
    t.left(1)


def turn_right():
    t.right(1)


def clear_screen():
    t.clear()
    t.up()
    t.home()
    t.down()


t = Turtle()

screen = Screen()

screen.listen()


screen.onkeypress(fun=move_forwards, key='Up')
screen.onkeypress(fun=move_backwards, key='Down')
screen.onkeypress(fun=turn_left, key='Left')
screen.onkeypress(fun=turn_right, key='Right')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
