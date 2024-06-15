import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

# Initialize Pygame and related modules
pygame.init()
pygame.font.init()
pygame.mixer.init()  # Initialize the mixer module

# Screen dimensions and settings
WIDTH = 500
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Global variables
current_screen = 0
scene_title_font = pygame.font.SysFont('Arial', 30)
current_song_index = 0
is_playing = False

# Load images
start = pygame.image.load('CPT/images/start.png')
start = pygame.transform.scale(start, (135, 70))
start_rect = start.get_rect(topleft=(170, 60))

settings = pygame.image.load('CPT/images/settings.png')
settings = pygame.transform.scale(settings, (150, 90))
settings_rect = settings.get_rect(topleft=(168, 130))

buy = pygame.image.load('CPT/images/buy.png')
buy = pygame.transform.scale(buy, (150, 80))
buy_rect = buy.get_rect(topleft=(167, 200))

check = pygame.image.load('CPT/images/check.png')
check = pygame.transform.scale(check, (70, 70))
check_rect = check.get_rect(topleft=(70,120))

# Settings screen images
back = pygame.image.load('CPT/images/back.png')
back = pygame.transform.scale(back, (200, 250))
back_rect = back.get_rect(topleft=(150, 40))

mute = pygame.image.load('CPT/images/mute.png')
mute = pygame.transform.scale(mute, (83, 90))
mute_rect = mute.get_rect(topleft=(170, 70))

volume_on = pygame.image.load('CPT/images/volume_on.png')
volume_on = pygame.transform.scale(volume_on, (90, 83))
volume_on_rect = volume_on.get_rect(topleft=(240, 77))

next_img = pygame.image.load('CPT/images/next.png')
next_img = pygame.transform.scale(next_img, (70, 70))
next_rect = next_img.get_rect(topleft=(250, 150))

previous_img = pygame.image.load('CPT/images/previous.png')
previous_img = pygame.transform.scale(previous_img, (70, 70))
previous_rect = previous_img.get_rect(topleft=(180, 150))

# Load songs
songs_list = [
    'CPT/Audio/Climbing.mp3',
    'CPT/Audio/Feels.mp3',
    'CPT/Audio/Gridlock.mp3',
    'CPT/Audio/Island_dream.mp3',
    'CPT/Audio/Unicorn_Heads.mp3'
]

# Functions to draw each screen
def menu_screen():
    screen.fill((31, 141, 79))
    scene_title = scene_title_font.render('The Night of Deforestation', True, (255, 255, 255))
    screen.blit(scene_title, (WIDTH // 5, 0))
    screen.blit(start, start_rect.topleft)
    screen.blit(settings, settings_rect.topleft)
    screen.blit(buy, buy_rect.topleft)

def official_game_code():
    screen.fill((128, 0, 0))
    scene_title = scene_title_font.render('Game code here', True, (255, 255, 255))
    screen.blit(scene_title, (0, 0))

def settings_screen():
    screen.fill((255, 255, 255))
    screen.blit(back, back_rect.topleft)
    screen.blit(check, check_rect.topleft)
    screen.blit(next_img, next_rect.topleft)
    screen.blit(previous_img, previous_rect.topleft)
    screen.blit(mute, mute_rect.topleft)
    screen.blit(volume_on, volume_on_rect.topleft)

def buy_screen():
    screen.fill((100, 100, 100))  # Example color
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

# Function to play a song
def play_song(index):
    global is_playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    pygame.mixer.music.load(songs_list[index])
    pygame.mixer.music.play()
    is_playing = True
    display_song = scene_title_font.render(f"Playing song: {songs_list[index]}", True, (0, 255, 255))
    screen.blit(display_song, (0, 0))
    print(f"Playing song: {songs_list[index]}")

# Function to handle next song
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs_list)
    play_song(current_song_index)

# Function to handle previous song
def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs_list)
    play_song(current_song_index)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if current_screen == 0:
                if start_rect.collidepoint(x,y):
                    current_screen = 1
                    print(current_screen)
                elif settings_rect.collidepoint(x,y):
                    current_screen = 2
                    print(current_screen)
                elif buy_rect.collidepoint(x,y):
                    current_screen = 3
                    print(current_screen)

            elif current_screen == 2:
                if check_rect.collidepoint(x,y):
                    current_screen = 0
                elif next_rect.collidepoint(x, y):
                    next_song()
                elif previous_rect.collidepoint(x, y):
                    previous_song()
                elif mute_rect.collidepoint(x, y):
                    pygame.mixer.music.pause()
                    print("Music paused")
                elif volume_on_rect.collidepoint(x, y):
                    pygame.mixer.music.unpause()
                    print("Music resumed")
            if current_screen == 3:
                if check_rect.collidepoint(x,y):
                    current_screen = 0
                # Where the shop code goes

        elif event.type == QUIT:
            running = False

    determine_screen()
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
