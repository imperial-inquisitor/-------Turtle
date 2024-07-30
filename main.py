from turtle import *
from random import *
from time import *

def rand_move():
    ran = randint(-150,400)
    rand = randint(-100,400)
    t.penup()
    t.goto(ran,rand)
    t.pendown()
    ran = randint(-150,400)
    rand = randint(-100,400)
    t1.penup()
    t1.goto(ran,rand)
    t1.pendown()

def catch(x,y):
    if IS_GAME:
        t.write("АААА!!!", font = ("SegoeUI",15, "normal"))
        t.n += 1 
def catchv(x,y):
    if IS_GAME:
        t1.write("АААА!!!", font = ("SegoeUI",15, "normal"))
        t1.n += 1
        ran = randint(-150,400)
        rand = randint(-100,400)
        t1.penup()
        t1.goto(ran,rand)
        t1.pendown()  
        

IS_GAME = True

t = Turtle()
t1 = Turtle()
t2 = Turtle()
t.speed(0)
t.shape("turtle")
t.color("brown")
t.n = 0
t.onclick(catch)
t1.speed(0)
t1.shape("turtle")
t1.color("grey")
t1.n = 0
t1.onclick(catchv)
t2.penup()
t2.goto(-700, -300)
t2.pendown()


ntime = time()
all_time = 0
while all_time <= 5:
    all_time = time() - ntime
    rand_move()
    t2.color("white")
    t2.begin_fill()
    t2.circle(30)
    t2.end_fill()
    t2.color("black")
    t2.write(int(all_time),font=("SegoeUI",25, "normal"))
    sleep(1)
IS_GAME = False

t.penup()
t.goto(0, 10)
t.pendown()
if t.n + t1.n >= 7:
    t.write("Ты победил", font = ("SegoeUI",25, "normal"))
else:
    t.write("Слабак", font = ("SegoeUI",25, "normal"))

done()