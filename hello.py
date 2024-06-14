# Scene Switching - Final

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_RIGHT, K_LEFT

pygame.init()
pygame.font.init()

WIDTH = 500
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Current Screen 0 aka Menu screen variables and images
start = pygame.image.load('CPT/images/start.png')
start = pygame.transform.scale(start, (135, 70))
start_rect = start.get_rect(topleft=(170, 60))

settings = pygame.image.load('CPT/images/settings.png')
settings = pygame.transform.scale(settings, (150, 90))
settings_rect = settings.get_rect(topleft=(168, 130))

buy = pygame.image.load('CPT/images/buy.png')
buy = pygame.transform.scale(buy, (150, 80))
buy_rect = buy.get_rect(topleft=(167, 200))

# Current screen 1,2,3 variable
check = pygame.image.load('CPT/images/check.png')
check = pygame.transform.scale(check, (70, 70))
check_rect = check.get_rect(topleft=(130,130))

# Current screen 1 (game)
# --> Add an exit button (exit.jpg) if applicable

#Current screen 2 (settings)
mute = pygame.image.load('CPT/images/mute.png')
mute = pygame.transform.scale(mute, (70, 70))
mute_rect = mute.get_rect(topleft=(190,130))

volume_on = pygame.image.load('CPT/images/volume_on.png')
volume_on = pygame.transform.scale(volume_on, (70, 70))
volume_on_rect = volume_on.get_rect(topleft=(260,130))

scene_title_font = pygame.font.SysFont('Arial', 30)
current_screen = 0

#Current screen 3 (shop)

# ---------------------------
def menu_screen():
    screen.fill((31,141,79)) 
    scene_title = scene_title_font.render('The Night of Deforestation', True, (255, 255, 255))
    screen.blit(scene_title, (WIDTH//5, 0))
    screen.blit(buy, buy_rect.topleft)
    screen.blit(settings, settings_rect.topleft)
    screen.blit(start, start_rect.topleft)

def official_game_code():
    screen.fill((128, 0, 0)) 
    scene_title = scene_title_font.render('Game code here', True, (255, 255, 255))
    screen.blit(scene_title, (0, 0))

def settings_screen():
    #blit links
    #blit music
    #blit lock
    screen.fill((255,255,255))
    screen.blit(check, check_rect.topleft)
    screen.blit(mute, mute_rect.topleft)
    screen.blit(volume_on, volume_on_rect.topleft)

def buy_screen():
    #IDK WHY DO WE NEED THIS??? --> someone made one 
    screen.blit(check, check_rect.topleft)

def determine_screen():
    if current_screen == 0:
        menu_screen()
    elif current_screen == 1:
        official_game_code()
    elif current_screen == 2:
        settings_screen()
    elif current_screen == 3:
        buy_screen()

def input_handling():
    running = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
                x,y = event.pos
                if current_screen == 0:
                    if start_rect.collidepoint(x,y):
                        running = false
                        current_screen = 1
                        print(current_screen)
                    elif settings_rect.collidepoint(x,y):
                        current_screen = 2
                        print(current_screen)
                    elif buy_rect.collidepoint(x,y):
                        current_screen = 3
                        print(current_screen)
                if current_screen == 2:
                    if mute_rect.collidepoint(x,y):
                        print('mute')
                        pass #mute
                    elif volume_on_rect.collidepoint(x,y):
                        print('volume on')
                        pass #unmute
                    elif check_rect.collidepoint(x,y):
                        current_screen = 0
                if current_screen == 3:
                    #Buy code 
                    pass

            elif event.type == QUIT:
                running = False
        determine_screen()

    
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    # screen.fill((255, 255, 255)) 

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
