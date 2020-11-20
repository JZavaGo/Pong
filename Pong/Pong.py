import turtle

#inicializando screen
wn = turtle.Screen()
wn.title("Pongo por noob")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score1 = 0
score2 = 0

#Paleta1
pA = turtle.Turtle()
pA.speed(0)
pA.shape("square")
pA.color("white")
pA.shapesize(stretch_wid=5, stretch_len=1)
pA.penup()
pA.goto(-350, 0)

#Paleta 2
pB = turtle.Turtle()
pB.speed(0)
pB.shape("square")
pB.color("white")
pB.shapesize(stretch_wid=5, stretch_len=1)
pB.penup()
pB.goto(350, 0)

#pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

#Pen Score
pen = turtle.Turtle()
pen.speed = 0
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

#Movimiento Paletas

def pA_Up():
    y = pA.ycor()
    y += 20
    pA.sety(y)

def pA_Down():
    y = pA.ycor()
    y -= 20
    pA.sety(y)

def pB_Up():
    y = pB.ycor()
    y += 20
    pB.sety(y)    

def pB_Down():
    y = pB.ycor()
    y -= 20
    pB.sety(y)

#Kb input
wn.listen()
wn.onkeypress(pA_Up, "w")
wn.onkeypress(pA_Down, "s")
wn.onkeypress(pB_Up, "Up")
wn.onkeypress(pB_Down, "Down")


#game loop
while True:
    wn.update()

    #Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Collision of the ball
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pB.ycor() + 40 and ball.ycor() > pB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pA.ycor() + 40 and ball.ycor() > pA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1            