import turtle
from random import randint
import time


screen = turtle.Screen()
screen.bgcolor("orange")
screen.title("catch the jack")

SCORE = 0



jack = turtle.Turtle()
score_turtle = turtle.Turtle()
time_turtle = turtle.Turtle()
hey_turtle = turtle.Turtle()


def hey_setup():
    hey_turtle.hideturtle()
    hey_turtle.color("white")
    hey_turtle.penup()
    hey_turtle.setposition(-370, 280)
    hey_turtle.write("hey! try to catch the jack!!", font=["Arial", 12])


def score_setup():
    score_turtle.speed(0)
    score_turtle.hideturtle()
    score_turtle.color("yellow")
    score_turtle.penup()
    score_turtle.setposition(0, 280)
    score_turtle.write(f"SCORE: {SCORE} ", align="center", font=["Arial", 15])


def jack_setup():
    jack.shape("turtle")
    jack.shapesize(1.5)
    jack.color("green")
    jack.speed(0)
    jack.penup()


def handler(x, y):
    global SCORE
    SCORE += 1
    score_turtle.clear()
    score_turtle.write(f"SCORE: {SCORE} ", align="center", font=["Arial", 15])


def timer_setup():
    time_turtle.speed(0)
    time_turtle.color("yellow")
    time_turtle.hideturtle()
    time_turtle.penup()
    time_turtle.setposition(0, 260)


def timer_motion(x):
    z = x
    for i in range(x):
        
        
        jack.goto(randint(-150,150), randint(-150,150))
        time_turtle.write(f"TIME: {x}", align="center", font=["Arial", 12])
        x -= 1
        i += 1
        time.sleep(1)
        time_turtle.clear()

        if i == z:
            time_turtle.write("GAME OVER", align="center", font=["Arial", 12])

        else:
            continue


turtle.tracer(0)
# set up functions
hey_setup()
jack_setup()
score_setup()
timer_setup()

turtle.tracer(1)

jack.onclick(handler)
timer_motion(10)
turtle.mainloop()
