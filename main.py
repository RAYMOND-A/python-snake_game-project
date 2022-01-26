import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # print("Nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increment_score()


    # Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
    # if head collides with any segment in the tail
        # trigger game over

# tim = Turtle(shape="square")
# tim.color("white")
# tim.pensize(width=20)
# print(tim.ycor())
#
# tam = Turtle(shape="square")
# tam.color("white")
# tam.pensize(width=20)
# tam.goto(-20, 0)
#
# tem = Turtle(shape="square")
# tem.color("white")
# tem.pensize(width=20)
# tem.goto(-40, 0)





screen.exitonclick()