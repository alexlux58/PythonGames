import turtle, winsound


score_a = 0
score_b = 0

wn = turtle.Screen()
wn.title("Pong by @Alex Lux")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)




# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .15
ball.dy = -0.15


def paddle_a_up():
    y = paddle_a.ycor()
    if paddle_a.ycor() > 300:
        y = -300
        paddle_a.sety(y)
    else:
        y += 20
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if paddle_a.ycor() < -300:
        y = 300
        paddle_a.sety(y)
    else:
        y -= 20
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if paddle_b.ycor() > 300:
        y = -300
        paddle_b.sety(y)
    else:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if paddle_b.ycor() < -300:
        y = 300
        paddle_b.sety(y)
    else:
        y -= 20
        paddle_b.sety(y)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

flag = True
# Main game loop
while flag:
    wn.update()

    # ---Move the ball---
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ---Border Check---
    # Top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # Bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    # Right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1
    # Left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() > 340 and (paddle_b.ycor() - 50) < ball.ycor() < (paddle_b.ycor() + 50):
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -340 and (paddle_a.ycor() - 50) < ball.ycor() < (paddle_a.ycor() + 50):
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
