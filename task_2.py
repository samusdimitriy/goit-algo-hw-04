import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        segment_length = length / 3
        koch_curve(t, segment_length, level - 1)
        t.left(60)
        koch_curve(t, segment_length, level - 1)
        t.right(120)
        koch_curve(t, segment_length, level - 1)
        t.left(60)
        koch_curve(t, segment_length, level - 1)

def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

level = int(input("Уровень рекурсии (0-6): "))
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.color("cyan")
t.penup()
t.goto(-150, 100)
t.pendown()
koch_snowflake(t, 300, level)
t.hideturtle()
screen.exitonclick()
