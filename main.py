from turtle import Screen
from player import Player, Finish
from score import playerScore
from obstacles import Obstacle
import time
import neat
import os
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

    # user_player = Player()
    # user_players = []

    reset_player = Finish()
    scoreboard = playerScore()

    window.tracer(0)
    obstacle = Obstacle()

    # Start listening for keystrokes
    # window.listen()
    # window.onkey(user_player.move_up, "Up")

# setup_game()


def main(genomes, config):
    setup_game()
    nets = []
    ge = []
    user_players = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        user_players.append(Player())
        g.fitness = 0
        ge.append(g)


    game_is_on = True
    while game_is_on:
        obstacle.move_obstacles()
        window.update()
        time.sleep(0.01)

        players_to_remove = []
        for x, user_player in enumerate(user_players):
            if user_player.ycor() >= 270:
                # print("Finished")
                user_player.take_player_to_start()
                scoreboard.increase_score()
                
                # increase fitness score by 5 if player reaches finish line
                ge[x].fitness += 5

                obstacle.spawn_next_obstacle_set()
                # obstacle.increase_speed()
            
            if user_player.ycor() <= -275:
                # print("player stuck at spawn", user_player.ycor())
                ge[x].fitness -= 10

        # print(user_player.current_player_y_position)

            nearest_x_diff, nearest_y_diff = obstacle.get_nearest_obstacle_distance(user_player)

            output = nets[x].activate([
                user_player.ycor(),
                nearest_x_diff,
                nearest_y_diff
            ])

            if output[0] > -0.5:
                # print(output[0], "output > 0.5")
                user_player.move_up()

            if obstacle.user_hit_obstacle(user_player.current_player_y_position):
                # print(f"HIT: y(player): {user_player.current_player_y_position}")

                # remove 1 from fitness score if collision
                ge[x].fitness -= 0.5
                players_to_remove.append(x)

                # window.clearscreen()
                # setup_game()
            
            ge[x].fitness += 0.1


        for i in reversed(players_to_remove):
            # print(f"Removing player {i}")
            user_players[i].hideturtle()
            user_players[i].clear()
            del user_players[i]
            # user_players.pop(i)
            nets.pop(i)
            ge.pop(i)

        obstacle.delete_past_obstacles()
        player_ys = [p.current_player_y_position for p in user_players]
        obstacle.spawn_new_obstacles_if_needed(player_ys)

        if len(user_players) == 0:
            print("All players are dead")
            window.clearscreen()
            game_is_on = False


    # window.exitonclick()

# main()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_path)
    
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 30)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)