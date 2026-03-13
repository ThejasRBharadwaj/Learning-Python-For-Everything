from turtle import Turtle, Screen
import time
from snake import Snake
from practise1 import Food

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 24, "normal"))    
        

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title("My Snake game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.goto(0,0)
        scoreboard.write("GAME OVER", align="center", font=("Times New Roman", 24, "normal"))
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.goto(0,0)
            scoreboard.write("GAME OVER", align="center", font=("Times New Roman", 24, "normal"))

        
screen.exitonclick()