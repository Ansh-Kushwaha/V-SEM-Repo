import math
import pygame

pygame.init()
screen = pygame.display.set_mode([1000, 500])
clock = pygame.time.Clock()
g = 9.8

class Ball(pygame.sprite.Sprite):
    def __init__(self, mass, color, pos, vel, rad):
        super().__init__()
        self.mass = mass
        self.color = color
        self.rad = rad
        self.pos = pos
        self.vel = vel

        self.image = pygame.Surface([rad * 2, rad * 2], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        pygame.draw.circle(self.image, self.color, (self.rad, self.rad), self.rad)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos



ball = Ball(30, [250, 0, 0], pygame.Vector2(500, 100), pygame.Vector2(0, 5), 30)
screen.blit(ball.image, ball.rect)

def main():
    running = True    
    while running:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill([0, 0, 0])
        ball.update()
        screen.blit(ball.image, ball.rect)

        pygame.display.flip()

main()