import pygame

class Planet():
    def __init__(self, solar_system, mass, x, y, color):
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        

        self.x_vel = 0
        self.y_vel = 0
        


class SolarSystem:
    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.display.set_caption("Planet Simulation")
        self.screen = pygame.display.set_mode([width, height])
        self.clock = pygame.time.Clock()

        self.bodies =[]

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(30)
    
    def add_body(self, body):
        self.bodies.append(body)
    def remove_body(self, body):
        self.bodies.remove(body)

    


SolarSystem(1000, 500)