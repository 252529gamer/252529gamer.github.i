import turtle

spiral = turtle.Turtle()
screen = turtle.Screen()
spiral.pencolor("blue")
spiral.speed(999999)
spiral.hideturtle()

for i in range(300):
  spiral.forward(i * 1)
  spiral.right(90)
  spiral.left(1)  

screen.clearscreen()
turtle.done()