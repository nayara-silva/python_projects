#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json# 

def turn_right():
    for turn in range(3):
        turn_left()
        
def check_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
while not is_facing_north():
    turn_left()
turn_right() 
while not at_goal():
    check_wall()
       
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
