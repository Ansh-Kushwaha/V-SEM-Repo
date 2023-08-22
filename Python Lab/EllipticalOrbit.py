import pygame
import math

au = 1.495978707e8
G = 6.6743e-11
width = 1000
height = 500

pygame.init()
pygame.display.set_caption("Planet Simulation")
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()

class Planet():
    def __init__(self, name, color, solar_system, mass, pos, vel):
        self.name = name
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.color = color

        solar_system.add_body(self)

    def draw(self):
        pygame.draw.circle(surface=screen, color=self.color, center=self.pos, radius = math.log(self.mass, 4))
    
    def update(self, nearby_bodies):
        self.getVelocity(nearby_bodies)
        print(self.pos.x, self.pos.y)
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y


    def getVelocity(self, nearby_bodies):
        for body in nearby_bodies:
            if body.name != self.name:
                dx = body.pos.x - self.pos.x
                dy = body.pos.y - self.pos.y
                angle = math.atan2(dy, dx)

                dd = math.sqrt((dx ** 2) + (dy ** 2))
                if dd == 0:
                    dd = 0.000001
                force = self.mass * body.mass / (dd ** 2)
                print(force)

                self.vel.x += (math.cos(angle) * force) / self.mass
                self.vel.y += (math.sin(angle) * force) / self.mass
    


class SolarSystem:
    def __init__(self):
        self.bodies = []

    def draw(self):
        screen.fill("black")
        for body in self.bodies:
            body.draw()
            
    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)


def main():
    s = SolarSystem()
    Sun = Planet('sun', [253, 184, 19], s, 1.9891e25, pygame.Vector2(width // 2, height // 2), pygame.Vector2(0, 0))
    P1 = Planet('earth', [0, 0, 160], s, 5.97219e5, pygame.Vector2((width // 2) + 2, height // 2), pygame.Vector2(0, 0))
    
    running = True
    
    while running:
        clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for body in s.bodies:
            body.update(s.bodies)
        s.draw()
        pygame.display.flip()

main()