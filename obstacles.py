from turtle import Turtle
from player import Player, Finish
import random
# COLORS = [(203, 228, 249), (205, 245, 246), (239, 249, 218), (249, 235, 223), (249, 216, 214), (214, 205, 234)]
COLORS2 = [(249, 155, 78), (48, 59, 147), (237, 77, 135), (250, 227, 190), (77, 185, 204), (99, 177, 114),
           (120, 146, 214), (250, 197, 142),  (235, 147, 104), (175, 74, 84), (255, 219, 105), (255, 115, 82),
           (227, 37, 63), (89, 130, 72), (187, 222, 102)]
n_blocks = 25
screen_size = 225
avg_block_dist = round(screen_size / n_blocks)
SPAWN_OBSTACLES_X_RANGE = [-280, 280]
SPAWN_HIDDEN_OBSTACLES_RANGE = [330, 860]


class Obstacle():
    def __init__(self):
        self.randomX_list = []
        self.obstacle_instances = []
        self.obstacle_speed_step_increase = 0.4
        # Spawn initial screen obstacles
        self.spawn_starting_obstacles(xleft=SPAWN_OBSTACLES_X_RANGE[0], xright=SPAWN_OBSTACLES_X_RANGE[1])
        # Spawn initial hidden obstacles
        self.spawn_starting_obstacles(xleft=SPAWN_HIDDEN_OBSTACLES_RANGE[0], xright=SPAWN_HIDDEN_OBSTACLES_RANGE[1])

    def spawn_starting_obstacles(self, xleft, xright):
        for yAvg in range(avg_block_dist, 2*screen_size, 2*avg_block_dist):
            # Create random X and Y values
            y_inc = yAvg + round(random.random() * avg_block_dist) - avg_block_dist - screen_size
            randomX = random.randint(xleft, xright)
            self.randomX_list.append(randomX)
            # print(f"x: {randomX} y: {y_inc}")

            # Create Obstacles
            obstacle_obj = Turtle()
            obstacle_obj.penup()
            obstacle_obj.shape("square")
            obstacle_obj.setpos(x=randomX, y=y_inc)
            obstacle_obj.shapesize(stretch_len=2, stretch_wid=1)
            obstacle_color = random.choice(COLORS2)
            obstacle_obj.color(obstacle_color)

            # Append Instance to list
            self.obstacle_instances.append(obstacle_obj)

    def move_obstacles(self):
        for obs in self.obstacle_instances:
            new_x_position = obs.xcor() - self.obstacle_speed_step_increase
            obs.speed(0.01)
            obs.setpos(x=new_x_position, y=obs.ycor())

    def increase_speed(self):
        self.obstacle_speed_step_increase += 0.3

    def spawn_next_obstacle_set(self):
        # max_x_value = max(self.randomX_list)
        # SPAWN_HIDDEN_OBSTACLES_RANGE[0] += 530
        # SPAWN_HIDDEN_OBSTACLES_RANGE[1] += 530
        # self.spawn_starting_obstacles(xleft=max_x_value, xright=max_x_value+530)
        # self.spawn_starting_obstacles(xleft=SPAWN_HIDDEN_OBSTACLES_RANGE[0], xright=SPAWN_HIDDEN_OBSTACLES_RANGE[1])

        for i in range(2):
            maxrightposition = 0
            for obs_objs in self.obstacle_instances:
                if obs_objs.xcor() >= maxrightposition:
                    maxrightposition = obs_objs.xcor() + 5

            maxspawnposition = maxrightposition + 530

            self.spawn_starting_obstacles(xleft=int(maxrightposition), xright=round(maxspawnposition))

    def user_hit_obstacle(self, player_y_pos):
        # print(player_y_pos)
        for obs_objs2 in self.obstacle_instances:
            if obs_objs2.xcor() <= 35 and obs_objs2.xcor() >= -35:
                if obs_objs2.ycor() < player_y_pos + 23 and obs_objs2.ycor() > player_y_pos - 16:
                    print(f"x(obstacle): {obs_objs2.xcor()}")
                    print(f"y(obstacle): {obs_objs2.ycor()}")
                    return True

    def delete_past_obstacles(self):
        for obs_objs3 in self.obstacle_instances:
            if obs_objs3.xcor() <= -340:
                self.obstacle_instances.remove(obs_objs3)
                print(f"Deleted: {obs_objs3}")