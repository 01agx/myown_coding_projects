from tkinter import *
import random


game_width = 700
game_height = 700
speed = 50
space_size = 50
body_parts = 3
snake_color = "#FFFB00"
food_color = "#FF0000"
background_color = "#000000"


class snake:
    pass

class food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass 

def check_collisions():
    pass 

def game_over():
    pass 


window = Tk()
window.title("snack game")
window.resizable(False, False)


score = 0 
direction = 'down'

label = label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()



window.mainloop()
