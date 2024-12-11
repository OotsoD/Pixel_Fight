import turtle
import random
import time
WIDTH,HEIGHT=800,600
screen = turtle.Screen()
screen.title("Pixel wars")
screen.bgcolor('black')
screen.setup(width=WIDTH,height=HEIGHT)
screen.tracer(0)
colors=['blue','green','cyan','purple','yellow','brown']
def create_players(colors):
    random.shuffle(colors)
    players=[]
    for i in range(2):
        color=colors[0]
        player = turtle.Turtle()
        player.shape('square')
        player.color(color)
        player.shapesize(stretch_len=2,stretch_wid=2)
        player.penup()
        if i==0 :
            player.setpos(-300,0)
        else:
            player.setpos(300,0)
        
        players.append(player)
    return players

def create_weapons(colors):
    random.shuffle(colors)
    weapons=[]

    for i in range(0,2):
        weapon= turtle.Turtle()
        color=colors[0]
        weapon.color(color)
        weapon.shape('triangle')
        weapon.penup()
        weapon.hideturtle()
        weapons.append(weapon)
    return weapons

def move_left():
    x= players[0].xcor()-20
    players[0].setx(max(-380,x))

def move_right():
    x= players[0].xcor()+20
    players[0].setx(min(380,x))

def move_up():
    y= players[0].ycor()+20
    players[0].sety(min(280,y))

def move_down():
    y= players[0].ycor()-20
    players[0].sety(max(-280,y))

def player_attack():
    weapon1.setpos(players[0].xcor()+40,players[0].ycor())
    weapon1.showturtle()
    screen.update()
    screen.ontimer(weapon1.hideturtle,200)

def collision(attacker,defender,health):
    if attacker.distance(defender)<30:
        health= health-10
    return health



players=create_players(colors)
weapons=create_weapons(colors)
weapon1=weapons[0]
weapon2=weapons[1]
player1_health=300
player2_health=300



screen.listen()
screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(player_attack, "space")


i,j=0,0
while player1_health > 0 and player2_health > 0:
    if i==25:
        
        players[1].setx(players[1].xcor() + random.choice([-20, 20]))
        players[1].sety(players[1].ycor() + random.choice([-20, 20]))
        i=0
        players[1].setx(max(-380, min(380, players[1].xcor())))
        players[1].sety(max(-280, min(280, players[1].ycor())))
    i=i+1
    if random.random() < 0.05:
        if j==5:
            j=0
            weapon2.goto(players[1].xcor() - 40, players[1].ycor())
            weapon2.showturtle()
            screen.update()
            screen.ontimer(weapon2.hideturtle, 200)
    j=j+1
    player1_health = collision(weapon2, players[0], player1_health)
    player2_health = collision(weapon1, players[1], player2_health)

    screen.title(f"YOUR Health: {player1_health} | COMPUTER Health: {player2_health}")
    
    screen.update()

winner = "YOU WINN" if player1_health > 0 else "COMPUTER WINS"
screen.title(f"Game Over! {winner} Wins!")
screen.mainloop()
time.sleep(5)