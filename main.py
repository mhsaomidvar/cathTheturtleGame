import turtle
import random
import time


screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("catch the jack")
SCORE = 0


jack = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()


def score():
    t1.speed(0)
    t1.hideturtle()
    t1.penup()
    t1.left(90)
    t1.forward(280)
    t1.write(f"SCORE: {SCORE} ",align="center", font=["Arial", 15])


# screen timer function
def timer(start):

    t2.speed(0)
    t2.hideturtle()
    t2.penup()
    t2.left(90)
    t2.forward(260)

    for i in range(start):

        t2.write(f"TIME: {start}", align="center", font=["Arial", 12])
        start -= 1
        time.sleep(1)
        t2.clear()


score()
timer(5)

turtle.mainloop()