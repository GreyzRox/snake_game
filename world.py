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
            cube = Entity(model  = 'cube',texture = 'texture/wood',position = (axe_x,-78,axe_y),scale = (10,60,10),collider = 'cube')
            liste_cube_ground.append(cube)
            
            axe_x += 10
        axe_y += 10
    real_ground = Entity (model = 'cube',texture = 'texture/sand',position = (70,-47,70),scale = (150,2,150),collider = 'cube')

def create_wall():
    return (Entity(model = 'cube',color = color.rgba(255,255,255,50),position = (70,-20,150),scale = (149,56,10),collider = 'box'),
            Entity(model = 'cube',color = color.rgba(255,255,255,50),position = (150,-20,70),scale = (149,56,10),rotation_y = 90,collider = 'box'),
            Entity(model = 'cube',color = color.rgba(255,255,255,50),position = (70,-20,-10),scale = (149,56,10),collider = 'box'),
            Entity(model = 'cube',color = color.rgba(255,255,255,50),position = (-10,-20,70),scale = (149,56,10),rotation_y = 90,collider = 'box'),
            PointLight(parent=camera, position=(0, 30, -20), color=color.white)
)

def init_player():
    head_player = (Entity(model = 'sphere',texture = 'white_cube',color = color.red,position = (10,10,10),scale = 10,))
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

def create_colonne():
    return ((Entity(model = 'cube',color = color.black,position = (-12.5,-20,-12.5),scale = (15,56,15))),
            (Entity(model = 'cube',color = color.black,position = (152.5,-20,-12.5),scale = (15,56,15))),
            (Entity(model = 'cube',color = color.black,position = (152.5,-20,152.5),scale = (15,56,15))),
            (Entity(model = 'cube',color = color.black,position = (-12.5,-20,152.5),scale = (15,56,15))))
