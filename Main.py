#Imports
import pygame
import math
import random

#initilizing pygame
pygame.init()

#Setting constants for window
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Fluid Simulation")

#setting constant rgb values for colors
WHITE = (255,255,255)

#Class used for creating particles
class Particle:
    #Constants for motion 
    SCALE = 1
    TIMESTEP = 1
    MASS = 2.99 * 10e23
    GRAVITY = 0.08

    #change in time used in calculating displacement and velocity
    delta = 0

    #Default constructor for particle 
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        self.x_vel = 0
        self.y_vel = 0

    def setX_vel(self,vel):
        self.x_vel = vel
    #Method to draw a circle to represent a particle
    def draw(self, win):
        x = self.x * self.SCALE
        y = self.y * self.SCALE
        pygame.draw.circle(surface=win, radius=self.radius, center=(x, y), color=self.color)

    #Method to update the position and velocity of the particle
    def updatePosition(self): 

        self.y_vel += self.GRAVITY * self.delta * self.SCALE

        self.y += self.y_vel * self.delta

        self.x += self.x_vel * self.delta

        self.delta += self.GRAVITY

        self.checkCollisionContainer()
      
    #Method to check for collisions of the container  
    def checkCollisionContainer(self):

        #To check for collisions for the top and bottom, then to bounce the particle off
        if (abs(self.y) > 500 - self.radius):
            self.y = 500 - self.radius
            self.y_vel *= -0.7    

        if (abs(self.y) < self.radius):
            self.y = self.radius
            self.y_vel *= 0.7

        #To check for collisions for the sides, then to bounce the particle off
        if (abs(self.x) > 500 - self.radius):
            self.x = 500 - self.radius
            self.x_vel *= -0.7    

        if (abs(self.x) < self.radius):
            self.x = self.radius
            self.x_vel *= 0.7
    
    def checkCollisionsParticles(self, particleList):
        
        for particle1 in particleList:
            for particle2 in particleList:
                if(particle1 != particle2):
                    if((particle1.x - particle2.x < particle1.radius + particle2.radius) or (particle1.y - particle2.y < particle1.radius + particle2.radius)):
                        particle1.x_vel = 1
                        particle2.x_vel = 1
                        particle1.x_vel *= -0.7
                        particle2.x_vel *= 0.7


#Method to created multiple particles at random positions
#@Return: ParticlesList: A list of Particle objects at random positions
def makeParticles(amount, radius, color, win):
    ParticlesList = list()

    #Loop to create the Particle objects
    for i in range(amount):
        Xrand = random.randint(11,480);
        Yrand = random.randint(11,480);
        ParticlesList.append(Particle(Xrand,Yrand,radius,color))

    #Loop to draw the particles
    for i in ParticlesList:
        i.draw(win)

    return ParticlesList


def main():
    run = True
    clock = pygame.time.Clock()

    WIN.fill(WHITE)
    pygame.display.update()

    particles = makeParticles(3,50,(173,216,230),WIN)
    pygame.display.update()
    time = 1
    deltat= 0
    velocity = 0
    xpos = 400
    ypos = 400
    while(run):
        clock.tick(60)

        WIN.fill(WHITE)
        pygame.display.update()

        for i in particles:
            i.updatePosition()
            i.checkCollisionsParticles(particles)
            i.draw(WIN)
            pygame.display.update()

       # pygame.draw.circle(surface=WIN,color=(173,216,230),center=(xpos,ypos),radius=50)
       # velocity += (0.0001)*deltat
        #ypos += velocity * deltat
        #deltat += time
        
       #if(abs(ypos) > 750):
            #ypos = 750
            #velocity *= -1 

        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()

main()
