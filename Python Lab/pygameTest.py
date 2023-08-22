import pygame

pygame.init()
width = 1000
height = 500

cenX = width // 2
cenY = height // 2

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Elliptical orbit")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(surface=screen, color=[252, 10, 100], center=[cenX, cenY], radius=50)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()