# Import Modules
import turtle
import time
import random
# Set Up the Game Window
window = turtle.Screen()
window.title("Snake")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)
# Game Variables
score = 0
high_score = 0
delay = 0.1
# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
segments = []
# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)


# Restarts Head Position, Removes all Segments and Resets the Score
def restart():
    time.sleep(1)
    delay = 0.1
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    global score
    score = 0
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


# Keyboard Bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")


# Main Game Loop
game_running = True
while game_running:
    window.update()
    # Check if Snake Head Collides with Borders
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        restart()
    # Check if Snake Head and Food Collided
    if head.distance(food) < 20:
        # ReSpawn Food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # Add a Segment
        add_segment()
        # Increase and Display the Score
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        # Decrease Delay
        delay -= 0.001
    # Snake Segment Management
        # Move each Segment to the Position of the Previous Segment (Reverse Order)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        # Move the First Segment to the Position of the Snake Head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    # Check if Snake Head Collides with its own Body(Segments)
    for segment in segments:
        if segment.distance(head) < 20:
            restart()
    time.sleep(delay)
