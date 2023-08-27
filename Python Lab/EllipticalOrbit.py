import pygame
import math

width = 1000
height = 500
center = pygame.Vector2(width // 2, height // 2)
G = 10

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
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
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

                # print(ax, ay)
        self.vel.x += ax
        self.vel.y += ay
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        pygame.draw.line(screen, self.color, self.rect.center, self.rect.center)


planets = []

sunPos = center
p1Pos = pygame.Vector2(center.x + 140, center.y)
p2Pos = pygame.Vector2(center.x, center.y + 210)

sun = Planet(4000, [253, 184, 19], sunPos, pygame.Vector2(0, -1.2), 40)
p1 = Planet(200, [51,194,254], p1Pos, pygame.Vector2(0, 19), 12)
# p2 = Planet(180, [193, 68, 14], p2Pos, pygame.Vector2(12, 0), 10)

screen.blit(sun.image, sun.rect)
screen.blit(p1.image, p1.rect)
# screen.blit(p2.image, p2.rect)

planets.append(sun)
planets.append(p1)
# planets.append(p2)

def main():
    running = True    
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for planet in planets:
            if planet == sun:
                continue
            planet.update(planets)
        screen.fill([0, 0, 0])
        for planet in planets:
            screen.blit(planet.image, planet.rect)

        pygame.display.flip()

main()