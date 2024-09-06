from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from world import (create_ground,create_wall,init_player,create_apple,destroy_apple,compteur)
import time
import random

player = FirstPersonController()
app = Ursina()
ground = create_ground()
wall = create_wall()
camera.fov = 120
head = init_player()
head.position = player.position
player.speed = 30
player.jump_height = 0
collision_tolerance = 3.0
liste_apple = []
apple = create_apple(liste_apple)
anti_nouvel_pomme = True
compteur_apple = 0
mon_texte = Text(text=compteur_apple, position=(0.7, 0.4), scale=5, color=color.white,font='font/cream_wish.ttf')

Sky()


def update():
    global apple, compteur_apple
    head.position = player.position + Vec3(0, 5.5, 0)

    
    distance = (head.position - apple.position).length()
    
    if distance < collision_tolerance:
        if len(liste_apple)==1:
            destroy_apple(liste_apple)
            print("Collision détectée avec la pomme!")
            if len(liste_apple)==0:
                create_apple(liste_apple)
                apple.position = liste_apple[0].position
                compteur_apple = compteur_apple + 1
                mon_texte.text = str(compteur_apple)

app.run()