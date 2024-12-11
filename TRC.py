import turtle 
import time
import random

WIDTH,HEIGHT=500,500
COLORS =['red','green','orange','purple','pink','brown','black','cyan','blue','yellow']



def get_racer_no():
    racers=0
    while True:
        racers=input("Enter Number of racers (2-10)")
        if racers.isdigit()==True:
            racers=int(racers)
            if(2<=racers<=10):
                break
            else:
                print("Enter a between (2-10)")
        else:
            print("Input is not numeric ... Enter again")              
    return racers


def create_turtles(colors,racers):
    turtles = []
    xr=0
    x = WIDTH // (racers + 1)
    for i , color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        
        xpos=x*(1+i)-WIDTH//2
        racer.setpos(xpos,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors,racers):
    turtles = create_turtles(colors,racers)

    while True:
        for racer in turtles:
            dist= random.randrange(1,20)
            racer.penup()
            racer.forward(dist)
            x,y=racer.pos()
            #print(x,y)
            if(y>=HEIGHT//2-10):
                return colors[turtles.index(racer)]




def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('RACE FT. TURTLES')


racers = get_racer_no()

init_turtle()
"""racer= turtle.Turtle()
racer.penup()
racer.speed(2)
racer.shape('turtle')#circle,arrow
racer.color('purple')
racer.forward(100)
racer.left(90)
racer.forward(100)
time.sleep(5)"""
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors,racers)
print(f'{winner} turtle has won')