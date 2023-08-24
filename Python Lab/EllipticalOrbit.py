import pygame
import math

width = 1000
height = 500
G = 1e-4

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

        self.image = pygame.Surface([rad * 2, rad * 2])
        self.image.fill([0, 0, 0, 0])
        self.rect = self.image.get_rect()

        pygame.draw.circle(self.image, self.color, (self.rad, self.rad), self.rad)

    def update(self, planets):
        for planet in planets:
            if planet != self:
                d = pygame.math.Vector2(self.pos).distance_to(planet.pos)
                if d == 0:
                    d = 0.000001
                angle = math.atan2((planet.pos.y - self.pos.y), (planet.pos.x - self.pos.x))
                force = G * self.mass * planet.mass / d * d
                ax = (force  * math.cos(angle)) / self.mass
                ay = (force  * math.sin(angle)) / self.mass
                # print(angle)

                self.vel.x += ax
                self.vel.y += ay

                self.pos.x += self.vel.x
                self.pos.y += self.vel.y

                print(self.pos)
                # print('Rect', self.rect)

planets = []

sunPos = pygame.Vector2(width // 2 - 60, height // 2 - 60)
p1Pos = pygame.Vector2(width // 2 + 200, height // 2 - 10)

sun = Planet(1000, [253, 184, 19], sunPos, pygame.Vector2(0, 0), 60)
p1 = Planet(4, [51,194,254], p1Pos, pygame.Vector2(0, 0), 10)

planets.append(sun)
planets.append(p1)

pygame.Surface.blit(screen, p1.image, p1.pos)
pygame.Surface.blit(screen, sun.image, sun.pos)


def main():
    running = True    
    while running:
        clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for planet in planets:
            planet.update(planets)
            screen.fill([0, 0, 0])
            pygame.display.update(planet.rect)
        pygame.display.flip()

main()