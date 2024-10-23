# Making a 2D Fluid Simulation Using Python
## Objective:
The primary objective of this project is to create a relatively physically accurate simulation of different fluids using Pygame as a visual library.  The idea is to read data such as velocity, kinetic energy, momentum, and other physical quantities to create data sets to train machine learning models. Then using real work data sets to test the models I could gauge how physically accurate my simulation is. 

## Inspiration:
The original inspiration for this project came from Sebastian Lague's coding adventure series on YouTube. 
The link to his original video can be found here: https://youtu.be/rSKMYc1CQHE?si=WYU_pnc0sXrbxJsl
Sebastian uses the Unity Engine which is much more powerful than Pygame.

## Background:

## Simulating a gas
I wanted to start by simulating a gas as it is easier to represent as each particle is independent of each other.

In the simplest form, a gas is a bunch of particles bouncing around a container and interacting with each other.

I started my simulation by creating a function to create a set amount of particles within the window.

    def  makeParticles(amount, radius, color, win):
	    ParticlesList  =  list()
		#Loop to create the Particle objects
		
		for  i  in  range(amount):
			Xrand  =  random.randint(PRAD  +  5 ,WIDTH  -  PRAD  - 5);
			Yrand  =  random.randint(PRAD  +  5,HEIGHT  -  PRAD  - 5);
			ParticlesList.append(Particle(Xrand,Yrand,radius,color))
			
			#Loop to draw the particles
			for  i  in  ParticlesList:
				i.draw(win)
				
		return  ParticlesList

Each particle is an object of the particle class and has attributes such as x position, y position, x velocity, and y velocity. When the constructor is called each particle is randomly assigned a x and y velocity as well as a random x and y position.

Basic Newtonian Motion can be represented by the equations:
v = at
p = vt
Where a is acceleration, v is velocity, p is position, and t is the change in time.

Using these equations we can make the particles move through a method of the particle class, called updatePostion

    def updatePosition(self):
	    self.y_vel  +=  self.y_acl  *  self.SCALE  *  self.TIMESTEP
	    
	    self.y  +=  self.y_vel  *  self.TIMESTEP
	    
	    self.x_vel  +=  self.x_acl  *  self.SCALE  *  self.TIMESTEP
	    
	    self.x  +=  self.x_vel  *  self.TIMESTEP
	    
	    self.delta  +=  self.TIMESTEP
	    
	    self.checkCollisionContainer()
	    
	    return self.delta

 
In the primary game loop we can call this method and the particles will move based on their velocity.

