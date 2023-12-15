import turtle



root = turtle.Screen()
tommy = turtle.Turtle()
tommy.speed(500)


def draw(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x, y-10*size)
    turtle.goto(x+10*size, y-10*size)
    turtle.goto(x+10*size, y-20*size)
    turtle.goto(x+30*size, y-20*size)
    turtle.goto(x+30*size, y-10*size)
    turtle.goto(x+20*size, y-10*size)
    turtle.goto(x+20*size, y)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(1000, 0)

def run():
    x,y = map(int, input('Enter coords (by space): ').split())
    c = input('Enter your color: ')
    s = int(input('Enter your size (like 1, 2, 3): '))
    draw(tommy, c, s, x, y)

run()

root.exitonclick()