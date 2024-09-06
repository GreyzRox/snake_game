from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from world import (create_ground,create_wall,init_player,create_apple)
import time
import random

player = FirstPersonController()
app = Ursina()
ground = create_ground()
#wall = create_wall()
camera.fov = 120
head = init_player()
head.position = player.position
direction = Vec3(0, 0, 0)
player.speed = 30
player.jump_height = 0
apple = create_apple()

Sky()


def update():
    head.position = player.position  + Vec3(0,5.2,0)

app.run()