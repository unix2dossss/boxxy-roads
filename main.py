from turtle import Screen
from player import Player, Finish
from score import playerScore
from obstacles import Obstacle
import time
SPAWN_OBSTACLES_X_RANGE = [-280, 280]


def setup_game():
    global window
    global user_player
    global obstacle
    global scoreboard
    global reset_player

    window = Screen()
    window.title("boxxy roads")
    window.setup(height=600, width=600)
    window.bgcolor("black")
    window.colormode(255)

    user_player = Player()
    reset_player = Finish()
    scoreboard = playerScore()

    window.tracer(0)
    obstacle = Obstacle()

    # Start listening for keystrokes
    window.listen()
    window.onkey(user_player.move_up, "Up")

setup_game()

game_is_on = True
while game_is_on:
    obstacle.move_obstacles()
    window.update()
    time.sleep(0.01)

    if user_player.ycor() >= 270:
        print("Finished")
        user_player.take_player_to_start()
        scoreboard.increase_score()
        obstacle.spawn_next_obstacle_set()
        obstacle.increase_speed()

    # print(user_player.current_player_y_position)

    if obstacle.user_hit_obstacle(user_player.current_player_y_position):
        print(f"HIT: y(player): {user_player.current_player_y_position}")
        window.clearscreen()
        setup_game()

    obstacle.delete_past_obstacles()

window.exitonclick()
