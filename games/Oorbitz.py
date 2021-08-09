from games.games import PycadeGame
from utils.vector import Vector
from utils.actions import Action
from utils.colors import RED,GREEN,ORANGE,BLUE,BLACK

import pygame
import random
import math
import numpy
import time

# Constants
planetSize = 40
cometSize = 15
rocketSize = 10
rocketSpeed = 15
gravity = .7

class Oorbitz(PycadeGame):
  @staticmethod
  def get_name():
    return "Oorbitz"

  def start(self):
    #variables local to Oorbitz
    self.isOver = False
    self.lives = 3
    cometGroup = []

    #variables accessible to other classes
    Oorbitz.surface = pygame.display.get_surface()
    Oorbitz.width = self.surface.get_width()
    Oorbitz.height = self.surface.get_height()
    Oorbitz.score = 0
    Oorbitz.rocketAngle = 90*math.pi/180
    Oorbitz.rocketPos = Vector(self.width/2 + planetSize*math.cos(self.rocketAngle), self.height/2 - planetSize*math.sin(self.rocketAngle))
    Oorbitz.rocketVel = Vector(0,0)
    Oorbitz.numComets = 0
    Oorbitz.maxComets = 2
    Oorbitz.cometGroup = []

    #flags
    self.rocketLaunched = False

    #creating comet starting positions along border of screen
    Oorbitz.cometPotPos = []
    for position in range(self.width+2*cometSize):
      Oorbitz.cometPotPos.append(Vector(position-cometSize,-cometSize)) #top
      Oorbitz.cometPotPos.append(Vector(position-cometSize,self.width+cometSize)) #bottom
    for position in range(self.height+2*cometSize):
      Oorbitz.cometPotPos.append(Vector(-cometSize,position-cometSize)) #left
      Oorbitz.cometPotPos.append(Vector(self.width+cometSize,position-cometSize)) #right
    
    Oorbitz.planet = Planet(planetSize)
    for comets in range(Oorbitz.maxComets):
      Comet()

  def update(self):  
    if Action.LEFT in self.currentActions and not self.rocketLaunched:
      self.rocketAngle += 0.2 #0.05*math.log(Oorbitz.numComets) + 0.1
    if Action.RIGHT in self.currentActions and not self.rocketLaunched:
      self.rocketAngle -= 0.2 #0.05*math.log(Oorbitz.numComets) + 0.1 
    #if Action.UP in self.currentActions:
    #if Action.DOWN in self.currentActions:
    if Action.BUTTON_1 in self.currentActions:
        self.rocketLaunched = True
        #setting rocket velocity to constant in direction of rocket angle
        self.rocketVel = Vector(math.cos(self.rocketAngle)*rocketSpeed,-math.sin(self.rocketAngle)*rocketSpeed)
        
    if self.rocketLaunched:
      #launching rocket by adding rocketVel
      self.rocketPos = self.rocketPos.add(self.rocketVel)
    else:
      #angle rocket along planet surface
      self.rocketPos = Vector(self.width/2 + planetSize*math.cos(self.rocketAngle), self.height/2 - planetSize*math.sin(self.rocketAngle))

    #delete rocket when out of bounds
    if self.isOutofBounds(self.rocketPos):
      self.rocketLaunched = False

    Oorbitz.cometGroupCopy = Oorbitz.cometGroup
    for cometNum in range(len(Oorbitz.cometGroupCopy)):
      #delete comet if out of bounds
      if self.isOutofBounds(Oorbitz.cometGroupCopy[cometNum].pos):
        Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum])
        newComet = Comet()
        continue

      #lose life if comet hits planet or hits rocket before launch
      if self.sphereCollision(self.planet.pos, self.planet.size, Oorbitz.cometGroupCopy[cometNum].pos, Oorbitz.cometGroupCopy[cometNum].size) or  (self.sphereCollision(self.rocketPos, rocketSize, Oorbitz.cometGroupCopy[cometNum].pos, Oorbitz.cometGroupCopy[cometNum].size) and not self.rocketLaunched):
        self.lives -=1
        Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum])
        newComet = Comet()
        continue

      if self.lives <=0:
        self.lose()

      #if rocket hits comet
      if self.sphereCollision(self.rocketPos, rocketSize, Oorbitz.cometGroupCopy[cometNum].pos, Oorbitz.cometGroupCopy[cometNum].size):
        self.score += round(self.gravRadius/10)*10
        Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum])
        newComet = Comet()
        continue
    
      for cometNum2 in range(len(Oorbitz.cometGroupCopy)):
        if cometNum2 != cometNum:
          #apply gravity for all combinations of comets
          self.applyGravity(Oorbitz.cometGroupCopy[cometNum], Oorbitz.cometGroupCopy[cometNum2])
          #remove comets if they collide
          if self.sphereCollision(Oorbitz.cometGroupCopy[cometNum].pos, Oorbitz.cometGroupCopy[cometNum].size, Oorbitz.cometGroupCopy[cometNum2].pos, Oorbitz.cometGroupCopy[cometNum2].size):
            newSize = math.sqrt(Oorbitz.cometGroupCopy[cometNum].size**2 + Oorbitz.cometGroupCopy[cometNum2].size**2)
            newPos = Oorbitz.cometGroupCopy[cometNum].pos.scalarMultiply(Oorbitz.cometGroupCopy[cometNum].size**2/(Oorbitz.cometGroupCopy[cometNum].size**2+Oorbitz.cometGroupCopy[cometNum2].size**2)).add(Oorbitz.cometGroupCopy[cometNum2].pos.scalarMultiply(Oorbitz.cometGroupCopy[cometNum2].size**2/(Oorbitz.cometGroupCopy[cometNum].size**2+Oorbitz.cometGroupCopy[cometNum2].size**2)))
            newVel = Oorbitz.cometGroupCopy[cometNum].vel.scalarMultiply(Oorbitz.cometGroupCopy[cometNum].size**2/(Oorbitz.cometGroupCopy[cometNum].size**2+Oorbitz.cometGroupCopy[cometNum2].size**2)).add(Oorbitz.cometGroupCopy[cometNum2].vel.scalarMultiply(Oorbitz.cometGroupCopy[cometNum2].size**2/(Oorbitz.cometGroupCopy[cometNum].size**2+Oorbitz.cometGroupCopy[cometNum2].size**2)))
            if cometNum2 < cometNum:
              Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum])
              Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum2])
            if cometNum2 > cometNum:
              Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum2])
              Oorbitz.cometGroup.remove(Oorbitz.cometGroupCopy[cometNum])
            newComet = Comet(newSize,newPos,newVel)
            newComet = Comet()
            continue
            continue
      self.applyGravity(Oorbitz.cometGroupCopy[cometNum], self.planet)
      

    return True #len(self.currentActions) > 0 

  def draw(self):
    if self.isOver:
      self.drawText("YOU SUCK", Vector(10, 10))
      self.drawText(f'Score Was {self.score}', Vector(10, 50))
      return
    #draw background
    self.drawRect(BLACK,Vector(0,0), self.screenSize, 0)
    #draw planet
    self.drawCircle(BLUE, self.planet.pos, self.planet.size)
    #draw comet
    for comets in range(len(Oorbitz.cometGroup)):
      self.drawCircle(ORANGE, self.cometGroup[comets].pos, self.cometGroup[comets].size)

    #draw rocket
    self.drawCircle(RED, self.rocketPos, rocketSize)
    #draw text
    self.drawText("Score", Vector(20,10))
    self.drawText(str(self.score), Vector(20,40))
    self.drawText("Lives", Vector(self.width-130,10))
    self.drawText(str(self.lives), Vector(self.width-80,40))

  def sphereCollision(self, sphere1: Vector, radius1: int, sphere2: Vector, radius2: int):
    if (sphere1.x - sphere2.x)**2 + (sphere1.y - sphere2.y)**2 < (radius1 + radius2)**2:
      return True
    else:
      return False
  
  def isOutofBounds(self, pos: Vector):
    return pos.x < -2*cometSize or pos.x > self.width + 2*cometSize or pos.y < -2*cometSize or pos.y > self.height + 2*cometSize

  def applyGravity(self, moon, planet):
    self.gravRadius = math.sqrt((moon.pos.x - planet.pos.x)**2 + (moon.pos.y - planet.pos.y)**2)
    gravMag = gravity/self.gravRadius**2 * planet.size**2
    gravNormal = Vector((planet.pos.x - moon.pos.x),(planet.pos.y-moon.pos.y)).scalarMultiply(1/self.gravRadius)
    deltaV = gravNormal.scalarMultiply(gravMag)
    moon.vel = moon.vel.add(deltaV)
    moon.pos = moon.pos.add(moon.vel)

  def lose(self):
    self.isOver = True

class Planet(Oorbitz):
  def __init__(self, radius: int):
    self.size = planetSize
    self.pos = Vector(Oorbitz.width/2,Oorbitz.height/2)
    self.vel = Vector(0,0)

class Comet(Planet):
  def __init__(self, size = None, pos = None, vel = None):
    if size and pos and vel:
      self.size = size
      self.pos = pos
      self.vel = vel
    else:
      self.pos = random.choice(Oorbitz.cometPotPos)
      self.size = random.randrange(10,25)
      Oorbitz.numComets +=1
      self.distance = math.sqrt((self.pos.x - Planet.planet.pos.x)**2 + (self.pos.y - Planet.planet.pos.y)**2)
      self.vel = Vector((Planet.planet.pos.x - self.pos.x),(Planet.planet.pos.y-self.pos.y)).scalarMultiply(1/self.distance)
      theta = random.choice([random.randrange(-8,-5)/10,random.randrange(5,8)/10]) 

      #applying random rotation of initial velocity
      self.vel.x = self.vel.x*math.cos(theta) - self.vel.y*math.sin(theta)
      self.vel.y = self.vel.x*math.sin(theta) + self.vel.y*math.cos(theta)
      self.vel = self.vel.scalarMultiply(random.randrange(1,10)) #+round(Oorbitz.score/500)))

    Oorbitz.cometGroup.append(self)

  def deleteComet(self):
    Oorbitz.cometGroup.remove(self)