import time
from turtle import Screen
from player import Player
from player import Player
from car_manager import CarManager
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move()
    # detects if it collides with a car
    for each_car in car.all_cars:
        if each_car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False
    # detect if it has crossed the finish line
    if player.finish_line_check():
        player.starting_line_position()
        car.level_up()
        scoreboard.update_scoreboard()
        scoreboard.increase_level()

screen.exitonclick()