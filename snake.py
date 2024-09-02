from ursina import *
from world import (create_ground,create_wall,init_player)
import time
import random


app = Ursina()
ground = create_ground()
wall = create_wall()
player = init_player()
camera.position = (player.x,player.y+10,player.z)
camera.fov = 100
camera.rotation_x = 20
direction = Vec3(0, 0, 0)
player_speed = 5   
Sky()

def update():
    global direction
    
    if held_keys['z']:
        direction = Vec3(0, 0, 1)
    elif held_keys['s']:
        direction = Vec3(0, 0, -1)
    elif held_keys['q']:
        direction = Vec3(-1, 0, 0)
    elif held_keys['d']:
        direction = Vec3(1, 0, 0)
    
    player.position += direction * time.dt * player_speed
    
    camera.position = (player.x, player.y + 20, player.z - 40)

app.run()