import math
import pygame

pygame.init()
screen = pygame.display.set_mode([1000, 500])
width = 1000
height = 500
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
        if self.pos.x < 0 or self.pos.x > width:
            self.vel.x = -self.vel.x
        if self.pos.y < 0 or self.pos.y > height:
            self.vel.y = -self.vel.y

        self.pos += self.vel
        self.rect.center = self.pos




ball1 = Ball(30, [250, 0, 0], pygame.Vector2(500, 100), pygame.Vector2(5, 1), 30)
ball2 = Ball(30, [120, 0, 0], pygame.Vector2(100, 200), pygame.Vector2(2, 1), 30)
ball3 = Ball(30, [100, 0, 0], pygame.Vector2(200, 400), pygame.Vector2(5, 6), 30)
ball4 = Ball(30, [53, 0, 0], pygame.Vector2(800, 300), pygame.Vector2(5, 2), 30)
# screen.blit(ball1.image, ball1.rect)
# screen.blit(ball2.image, ball2.rect)
# screen.blit(ball3.image, ball3.rect)
# screen.blit(ball4.image, ball4.rect)

balls = []

balls.append(ball1)
balls.append(ball2)
balls.append(ball3)
balls.append(ball4)

def main():
    running = True    
    while running:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill([0, 0, 0])
        for ball in balls:
            ball.update()
            screen.blit(ball.image, ball.rect)

        pygame.display.flip()

main()