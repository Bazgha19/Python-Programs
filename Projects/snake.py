import turtle as t
import random as rd
import time as ti

t.bgcolor('Yellow')

caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

food=t.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.speed()
food.hideturtle()

''' Instead of circle we can shape the food into leaf shape
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
'''
text_turtle=t.Turtle()
text_turtle.write('Press Space to Start',align='center',font=('Arial',34,'bold'))
text_turtle.hideturtle()

score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)



def outside_window():
    left_wall=-t.window_width()/2
    right_wall=t.window_width()/2
    top_wall=t.window_height()/2
    bottom_wall=-t.window_height()/2
    (x,y)=caterpillar.pos()
    outside= x<left_wall or x>right_wall or y>top_wall or y<top_wall
    return outside  
    
    
def place_food():
    food.hideturtle()
    food.setx(rd.randint(-200,200))
    food.sety(rd.randint(-200,200))
    

    
def game_over():
    caterpillar.color('yellow')
    food.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('Game Over',align='center',font='bold')
    

    


def display_score():
    score_turtle.clear()
    score_turtle.penup()
    x=(t.window_width()/2)
    y=(t.window_height()/2)
    score_turtle.write(str(current_score),align='right',font=('Ariel',18,'bold'))


def start_game():
    global game_started
    if game_started:
        return
    game_started=True
    score=0
    text_turtle.clear()
    
    caterpillar_speed=2
    caterpillar_length=3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    
    
t.onkey(start_game,'space')
t.listen()
t.mainloop()

ti.sleep(3)