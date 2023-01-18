# Gerekli kütüphaneler
import button
import pygame 
import sys
import math

en= 940
boy = 700
kirmizi = (225,0,0)
beyaz = (225,225,225)
mavi = (0,0,225)
siyah = (0,0,0)
agirlik=5

pygame.init()

# ekran tanımlama
screen = pygame.display.set_mode((en, boy))

# Choose Font
font = pygame.font.SysFont("arial", 50)

# butonlar
dünya_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\yuvarlakdünya.png")
ay_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\yuvarlakay.png")
cikis_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\button_quit.png")
tofaş_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\tofaş.png")

object1 = pygame.Rect(20, 50, 20, 50)
object2 = pygame.Rect(20, 50, 20, 50)
object3 = pygame.Rect(20, 50, 20, 50)
object4 = pygame.Rect(20, 50, 20, 50)   
obstacle = pygame.Rect(350, 500, 800, 50)

dünya_butonu = button.Button(90, 250, dünya_resmi, 1)
ay_butonu = button.Button(700, 250, ay_resmi, 1)
cikis_butonu = button.Button(400, 600, cikis_resmi, 1)
tofaş_butonu = button.Button(735,0,tofaş_resmi,1)

# basic font for user typed
user_text = ''

gelenagirlik = 0

  
# create rectangle
input_rect = pygame.Rect(150, 200, 200, 80)

  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

input_active = False


# States
moving = False
game_paused = True
run = True
menu_state = "main"



# Event Loop
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            object1.collidepoint(event.pos)
            moving = True
            if input_rect.collidepoint(event.pos):
                buton_active = True
            else:
                buton_active = False
        elif event.type == pygame.MOUSEMOTION and moving:
            object1.move_ip(event.rel)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode  
                gelenagirlik = int(user_text)
            
    if game_paused:
        
        if menu_state == "main":
            screen.fill((255,0,0))
            background = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\uzaytrnindir.jpg") 
            screen.blit(background, (0,0))
            arkaplanterazi =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\giriştahteravallisi.png")
            screen.blit(arkaplanterazi,(500,550))
      
            if dünya_butonu.draw(screen):
                menu_state = "earth"
                game_paused = False
            if ay_butonu.draw(screen):
                menu_state = "moon"
                game_paused = False
            if cikis_butonu.draw(screen):
                run = False
          
    else:
        if menu_state == "earth":
            # background
            background = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\Dünya.jpg") 
            screen.blit(background, (0,0))
            tahteravalli =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\seesawdüz.png")
            screen.blit(tahteravalli,(150,220))
            küp_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\küp.png")
            screen.blit(küp_resmi,(600,400))
            ok_isareti =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\ok1.png")
            screen.blit(ok_isareti,(150,280))
            geri_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\button_back.png")
            geri_butonu = button.Button(0, 0, geri_resmi, 1)
           
            if input_active:
                color = color_active
            else:
                color = color_passive
                
            
           
           
                if geri_butonu.draw(screen):
                    menu_state = "main" 
                    game_paused = True
                    user_text = ""
            pygame.draw.rect(screen, color, input_rect)
        
            text_surface = font.render(user_text, True, (225,225,0))
            
            screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            
            
           
            if gelenagirlik>agirlik*10:
                
                menu_state = "earthup"
                game_paused = False
            planet_text = font.render("5 kg", True, (255, 0, 0))
            screen.blit(planet_text, (650,450))

        elif menu_state == "moon":
            # background
            background = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\aydunya.png")
            screen.blit(background, (0, 0))
            tahteravalli =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\seesawdüz.png")
            screen.blit(tahteravalli,(150,220))
            küp_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\küp.png")
            screen.blit(küp_resmi,(600,400))
            ok_isareti =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\ok1.png")
            screen.blit(ok_isareti,(150,280))
            geri_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\button_back.png")
            geri_butonu = button.Button(0, 0, geri_resmi, 1)
            if geri_butonu.draw(screen):
                menu_state = "main" 
                game_paused = True
            if input_active:
                color = color_active
            else:
                color = color_passive
            
            if geri_butonu.draw(screen):
                menu_state = "main" 
                game_paused = True
                user_text = ""

            pygame.draw.rect(screen, color, input_rect)
        
            text_surface = font.render(user_text, True, (225,225,0))
            
            screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            
        
            if gelenagirlik>agirlik*2:
                
                menu_state = "moonup"
                game_paused = False
                
                
            
            planet_text = font.render("5 kg", True, (255, 0, 0))
            screen.blit(planet_text, (650,450))



       
        
        elif  menu_state == "earthup" :
            background = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\Dünya.jpg") 
            screen.blit(background, (0,0))
            tahteravalli =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\seesawdönük.png")
            screen.blit(tahteravalli,(150,220))
            küp_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\küp.png")
            screen.blit(küp_resmi,(600,300))
            ok_isareti =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\ok1.png")
            screen.blit(ok_isareti,(150,350))
            geri_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\button_back.png")
            geri_butonu = button.Button(0, 0, geri_resmi, 1)
           
            user_text = str(gelenagirlik)

        
        if  geri_butonu.draw(screen):
            menu_state = "main" 
            game_paused = True
            user_text = ""

            

        
            pygame.draw.rect(screen, color, input_rect)
            game_paused = True
            text_surface = font.render(user_text, False, (225,225,0))
            
            screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            # game_paused = True
        elif  menu_state == "moonup" :
            background = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\aydunya.png") 
            screen.blit(background, (0,0))
            tahteravalli =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\seesawdönük.png")
            screen.blit(tahteravalli,(150,220))
            küp_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\küp.png")
            screen.blit(küp_resmi,(600,300))
            ok_isareti =pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\ok1.png")
            screen.blit(ok_isareti,(150,350))
            geri_resmi = pygame.image.load("C:\\Users\\ozdem\\Desktop\\proje\\resimler\\button_back.png")
            geri_butonu = button.Button(0, 0, geri_resmi, 1)
          
            user_text = str(gelenagirlik)

        if geri_butonu.draw(screen):
            menu_state = "main" 
            game_paused = True
            user_text = ""   


          
            pygame.draw.rect(screen, color, input_rect)
            
            text_surface = font.render(user_text, False, (225,225,0))
            
            screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
            game_paused = True   
          

    pygame.display.update()
