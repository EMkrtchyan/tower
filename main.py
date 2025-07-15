import pygame
import sys

# functions

# initialize pygame
pygame.init()

# set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower")

# colors 

background = (255,242,204)
wood = (198,176,140)
disks = [
    (148, 0, 211),   # Violet
    (75, 0, 130),    # Indigo
    (0, 0, 255),     # Blue
    (0, 255, 0),     # Green
    (255, 255, 0),   # Yellow
    (255, 127, 0),   # Orange
    (255, 0, 0)      # Red
]


# set up clock
clock = pygame.time.Clock()
FPS = 60  # Frames per second

# rod arrays

firstRod = [0,1,2,3,4,5,6]
secondRod = []
thirdRod = []

rods = [firstRod,secondRod,thirdRod]


# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game logic

    # drawing code
    screen.fill(background)  # Fill screen

    # draw rods -|-|-|- divide the screen into 7 secments 
    rodBaseW = WIDTH//7
    rodBaseH = HEIGHT//12

    rodW = WIDTH//32
    rodH = HEIGHT//4


    diskH = rodH//8
    
    for i in range(3):
        pygame.draw.rect(screen, wood, (rodBaseW+i*rodBaseW*2, 10*rodBaseH, rodBaseW, rodBaseH),border_radius=16)
        pygame.draw.rect(screen, wood, (rodBaseW+rodBaseW//2-rodW//2+i*rodBaseW*2, 10*rodBaseH-rodH, rodW, rodH),border_top_left_radius=16,border_top_right_radius=16)
    
    for j,rod in enumerate(rods):
        for i, disk in enumerate(rod):
            diskW = int(rodBaseW - (disk / 8) * (rodBaseW - rodW))
            rodX = rodBaseW + rodBaseW // 2 + j * rodBaseW*2
            diskX = rodX - diskW // 2
            diskY = 10 * rodBaseH - (i + 1) * diskH
            pygame.draw.rect(screen, disks[disk], (diskX, diskY, diskW, diskH), border_radius=8)



    # update display
    pygame.display.flip()

    # cap the frame rate
    clock.tick(FPS)

# clean up
pygame.quit()
sys.exit()


