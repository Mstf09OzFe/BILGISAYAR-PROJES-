import pygame as pg
import sys
import random

def top_olustur():
    global en , boy
    cap = random.randrange(0,100)
    x= random.randrange(cap,en-cap)
    y= random.randrange(cap,boy-cap)
    x = en//2
    y = boy//2
    x_speed =random.randrange(-5,20)
    y_speed =random.randrange(-5,20)
    renk = random.randrange(0,225), random.randrange(0,225), random.randrange(0,225)
    return[x,y,x_speed,y_speed,cap,renk]

def konum_guncelle(top):
    top[0] += top[2]
    top[1] += top[3]

    if top[0] >= en - top[3] or top[0]<= top[4] :
        top[2] = -1
    if top[1] >= boy- top[4] or top[1] <= 0 + top[4] :
       top[3]= -1

pg.init()

en , boy = 800 , 750
siyah = 0 , 0 , 0 # RGB 0- 255 
beyaz = 255 , 255 , 255 
kırmızı = 255 , 0 , 0
gri = 100 , 100 , 100
acıkmor = 238 , 130 , 238
clock = pg.time.Clock()

ekran = pg.display.set_mode( ( en,boy) )

toplar =[]

for i in range(1000) :
    toplar.append(top_olustur())

while True :
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(acıkmor)

    for i in range(len(toplar)) :


        pg.draw.circle(ekran,toplar[i][5],( toplar[i][0] , toplar[i][1]) ,  toplar[i][4] )

        konum_guncelle( toplar[i])

    pg.display.flip()
    clock.tick(60)