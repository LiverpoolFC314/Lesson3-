import pgzrun
import random
WIDTH = 600
HEIGHT =600
sam = Actor("alien1")
sam.x = 300
sam.y = 300
score = 0 
message = "click on the alien"

def draw():
    screen.fill("Blue")
    sam.draw()
    screen.draw.text(str(score),(300,50),color="black")
    screen.draw.text(message,(300,70),color="black")
    
def update():
    pass
def on_mouse_down(pos):
    global message 
    global score

    print(pos)
    if sam.collidepoint(pos):
        sam.x = random.randint(0,600)
        sam.y = random.randint(0,600)
        score= score+1
        message = "Good Shot!"
    else:
        message = "Nice Try"
        
pgzrun.go()


    