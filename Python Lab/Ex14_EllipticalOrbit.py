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
    def __init__(self, mass, type, color, pos, vel, rad):
        super().__init__()
        self.mass = mass
        self.type = type
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
            # if self.type == 'moon' and planet.type == 'sun':
            #     continue
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
p1Pos = pygame.Vector2(center.x + 190, center.y)
m1Pos = pygame.Vector2(center.x + 185, center.y)

sun = Planet(4000, 'sun', [253, 184, 19], sunPos, pygame.Vector2(0, 0), 30)
p1 = Planet(200, 'planet', [51,194,254], p1Pos, pygame.Vector2(0, 15.4), 10)
m1 = Planet(165, 'moon', [193, 193, 193], m1Pos, pygame.Vector2(0, 13), 4)

# screen.blit(sun.image, sun.rect)
# screen.blit(p1.image, p1.rect)
# screen.blit(p2.image, p2.rect)

planets.append(sun)
planets.append(p1)
planets.append(m1)

def main():
    running = True    
    while running:
        clock.tick(4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for planet in planets:
            if planet == sun:
                continue
            planet.update(planets)
            pass
        # screen.fill([0, 0, 0])
        for planet in planets:
            screen.blit(planet.image, planet.rect)

        pygame.display.flip()

main()