import pygame
import math

width = 1000
height = 500
G = 70

pygame.init()
pygame.display.set_caption("Planet Simulation")
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, color, pos, vel, rad):
        super().__init__()
        self.mass = mass
        self.color = color
        self.pos = pos
        self.vel = vel
        self.rad = rad

        self.image = pygame.Surface([rad * 2, rad * 2], pygame.SRCALPHA)
        # self.image.fill([0, 0, 0])
        self.rect = self.image.get_rect()
    
        pygame.draw.circle(self.image, self.color, (self.rad, self.rad), self.rad)

    def update(self, planets):
        self.rect.center = self.pos
        ax, ay = 0, 0
        for planet in planets:
            if planet != self:
                d = pygame.math.Vector2(self.pos).distance_to(planet.pos)
                if d == 0:
                    d = 0.000001
                dy = planet.pos.y - self.pos.y
                dx = planet.pos.x - self.pos.x
                # angle = pygame.math.Vector2(self.pos).angle_to(planet.pos) * math.pi / 180
                angle = math.atan2(dy, dx)
                force = G * self.mass * planet.mass / (d * d)
                ax += (force  * (dx / d)) / self.mass
                ay += (force  * (dy / d)) / self.mass 
                print(ax, ay)
        self.vel.x += ax
        self.vel.y += ay

        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

planets = []

sunPos = pygame.Vector2(width // 2, height // 2)
p1Pos = pygame.Vector2(width // 2, height // 2 - 200)

sun = Planet(200, [253, 184, 19], sunPos, pygame.Vector2(-0.2, 0), 80)
p1 = Planet(4, [51,194,254], p1Pos, pygame.Vector2(10, 0), 10)
m1 = Planet(1, [43, 234, 123], m1.pos, pygame)

planets.append(sun)
planets.append(p1)

group = pygame.sprite.Group()
group.add(sun)
group.add(p1)

pygame.Surface.blit(screen, p1.image, p1.pos)
pygame.Surface.blit(screen, sun.image, sun.pos)


def main():
    running = True    
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for planet in planets:
            planet.update(planets)
        screen.fill([0, 0, 0])
        for planet in planets:
            screen.blit(planet.image, planet.rect)

        pygame.display.flip()

main()