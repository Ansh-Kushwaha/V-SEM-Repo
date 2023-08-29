import math
import random
import pygame
import numpy as np

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
        self.radius = rad
        self.pos = pos
        self.vel = vel

        self.image = pygame.Surface([rad * 2, rad * 2], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)

    def update(self, balls):
        if self.pos.x - self.radius < 0 or self.pos.x + self.radius > width:
            self.vel.x = -self.vel.x
        if self.pos.y - self.radius < 0 or self.pos.y + self.radius > height:
            self.vel.y = -self.vel.y

        self.pos += self.vel
        self.rect.center = self.pos

        for ball in balls:
            if ball != self:
                if self.pos.distance_to(ball.pos) <= self.radius + ball.radius:
                    dx = ball.pos.x - self.pos.x
                    dy = ball.pos.y - self.pos.y

                    angle = math.atan2(dy, dx)
                    u1 = self.vel.x * math.cos(angle) + self.vel.y * math.sin(angle)
                    u2 = ball.vel.x * math.cos(angle) + ball.vel.y * math.sin(angle)

                    p1 = self.mass * u1
                    p2 = ball.mass * u2
                    print(p1, p2)

                    a = np.array([[1, -1], [ball.mass, self.mass]])
                    b = np.array([u2 - u1, p2 + p1])
                    x = np.linalg.solve(a, b)
                    print(x)

                    ball.vel.x = x[1] * math.cos(angle)
                    ball.vel.y = x[1] * math.sin(angle)
                    self.vel.x = x[0] * math.cos(angle)
                    self.vel.y = x[0] * math.sin(angle)

            self.pos.x += self.vel.x
            self.pos.y += self.vel.y
            self.rect.center = self.pos
                    


                    
                    





ball1 = Ball(5, [250, 0, 0], pygame.Vector2(100, 228.787), pygame.Vector2(5, 2), 50)
ball2 = Ball(3, [200, 200, 200], pygame.Vector2(900, 271.213), pygame.Vector2(-3, 3), 30)

balls = []

balls.append(ball1)
balls.append(ball2)

def main():
    running = True    
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill([0, 0, 0])
        for ball in balls:
            ball.update(balls)
            screen.blit(ball.image, ball.rect)

        pygame.display.flip()

main()