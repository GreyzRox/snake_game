from ursina import *
import random


axe_x = 0
axe_y = 0
liste_cube_ground = []
length_player = []

def create_ground():
    global axe_x,axe_y
    for i in range(15):
        axe_x = 0
        for j in range(15):
            cube = Entity(model  = 'cube',texture = 'white_cube',position = (axe_x,-50,axe_y),scale = (10,10,10),collider = 'box')
            liste_cube_ground.append(cube)
            
            axe_x += 10
        axe_y += 10
    print(liste_cube_ground)

def create_wall():
    return (Entity(model = 'cube', texture = 'white_cube',color = color.blue,position = (70,0,150),scale = (150,50,10),collider = 'mesh'),
            Entity(model = 'cube', texture = 'white_cube',color = color.blue,position = (150,0,70),scale = (150,50,10),rotation_y = 90,collider = 'mesh'),
            Entity(model = 'cube', texture = 'white_cube',color = color.blue,position = (70,0,-10),scale = (150,50,10),collider = 'mesh'),
            Entity(model = 'cube', texture = 'white_cube',color = color.blue,position = (-10,0,70),scale = (150,50,10),rotation_y = 90,collider = 'mesh'))

def init_player():
    head_player = (Entity(model = 'sphere',texture = 'white_cube',color = color.red,position = (10,10,10),scale = 10))
    return head_player

def create_apple(liste):
    apple_position = (random.randint(1, 14) * 10, -40, random.randint(1, 14) * 10)
    apple = Entity(model='cube', texture='white_cube', color=color.green, position=apple_position, scale=(10, 10, 10))
    liste.append(apple)
    return apple

def destroy_apple(liste):
    for apple in liste:
        apple.disable()
    liste.clear()



def compteur(i):
    i = i + 1
    return i