import pygame        
import pygame.surface
pygame.init()   

ekran=pygame.display.set_mode((1280,720))  

pygame.display.set_caption("Tahterevalli Denge Simülasyonu")     

background=pygame.image.load("C:\\Users\\ozdem\\Desktop\\oto_22\\PYGAME FOTO\\media_16ad2258cac6171d66942b13b8cd4839f0b6be6f3.png")   
background==1
icon = pygame.image.load("C:\\Users\\ozdem\\Desktop\\oto_22\\PYGAME FOTO\\media_16ad2258cac6171d66942b13b8cd4839f0b6be6f3.png")
   
pygame.display.set_icon(icon)


white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)

run=True
while run:
    ekran.fill((122,20,240))  
    ekran.blit(background(0,0))  


    for event in pygame.event.get():     
        if event.type==pygame.QUIT:
            run=False                                      

    pygame.display.update()