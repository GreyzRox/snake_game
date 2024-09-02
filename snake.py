from ursina import *
from world import (create_ground,create_wall,init_player)
import time
import random


app = Ursina()
ground = create_ground()
wall = create_wall()
player = init_player()
camera.position = (player.x,player.y+10,player.z)
camera.fov = 120
camera.rotation_x = 15
direction = Vec3(0, 0, 0)
player_speed = 10
Sky()

def update():
    global direction
    
    if held_keys['up arrow']:
        direction = Vec3(0, 0, 1)
        player.rotation_y = min(player.rotation_y + player_speed * time.dt, 0)
        camera.rotation_y = min(camera.rotation_y + player_speed * time.dt, 0)
    elif held_keys['down arrow']:
        direction = Vec3(0, 0, -1)
        player.rotation_y = max(player.rotation_y - player_speed * time.dt, 180)
        camera.rotation_y = max(camera.rotation_y - player_speed * time.dt, 180)
    elif held_keys['left arrow']:
        direction = Vec3(-1, 0, 0)
        player.rotation_y = max(player.rotation_y - player_speed * time.dt, -90)
        camera.rotation_y = max(camera.rotation_y - player_speed * time.dt, -90)
    elif held_keys['right arrow']:
        direction = Vec3(1, 0, 0)
        player.rotation_y = min(player.rotation_y + player_speed * time.dt, 90)
        camera.rotation_y = min(camera.rotation_y + player_speed * time.dt, 90)

    
    player.position += direction * time.dt * player_speed
    
    camera.position = (player.x, player.y + 7, player.z+2)
    print(player.rotation_y)

app.run()