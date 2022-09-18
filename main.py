from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width = 600, height = 600)
screen.mode("logo")
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# snake = []
# PACE = 20
# start_pos = 0
# for a in range(3):
#     snake.append(Turtle())
#     snake[a].penup()
#     snake[a].shape("square")
#     snake[a].shapesize(1,1,0)
#     snake[a].color("white")
#     snake[a].goto(start_pos, 0)
#     start_pos -= PACE

snake = Snake(9)
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


games_is_on = True
while games_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move('forward')

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.add_segment()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() > 280:
        games_is_on = False
        score.game_over()

    for segment in snake.body[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            games_is_on = False
            score.game_over()

    # for part in range(len(snake) - 1 , 0, -1):
    #     new_x = snake[part - 1].xcor()
    #     new_y = snake[part - 1].ycor()
    #     snake[part].goto(new_x,new_y)
    #
    # snake[0].forward(20)




screen.exitonclick()
