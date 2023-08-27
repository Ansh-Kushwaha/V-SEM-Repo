import math
import random
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

    def update(self, balls):
        if self.pos.x - self.rad < 0 or self.pos.x + self.rad > width:
            self.vel.x = -self.vel.x
        if self.pos.y - self.rad < 0 or self.pos.y + self.rad > height:
            self.vel.y = -self.vel.y

        for ball in balls:
            if ball != self:
                d = pygame.math.Vector2(self.pos).distance_to(ball.pos)
                if d <= self.rad + ball.rad:
                    self.vel.x = -self.vel.x
                    self.vel.y = -self.vel.y
                    ball.vel.x = -ball.vel.x
                    ball.vel.y = -ball.vel.y

        self.pos += self.vel
        self.rect.center = self.pos




ball1 = Ball(30, [250, 0, 0], pygame.Vector2(500, 100), pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5)), 30)
ball2 = Ball(20, [200, 200, 200], pygame.Vector2(100, 200), pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5)), 20)
ball3 = Ball(40, [100, 230, 0], pygame.Vector2(200, 400), pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5)), 40)
ball4 = Ball(45, [53, 0, 241], pygame.Vector2(800, 300), pygame.Vector2(random.randint(-5, 5), random.randint(-5, 5)), 45)
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
            ball.update(balls)
            screen.blit(ball.image, ball.rect)

        pygame.display.flip()

main()