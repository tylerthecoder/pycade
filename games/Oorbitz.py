from games.games import PycadeGame
from utils.vector import Vector
from utils.actions import Action
from utils.colors import RED,GREEN,ORANGE,BLUE,BLACK

import pygame
import random
import math

# Constants
planetSize = 40
cometSize = 15
rocketSize = 10
rocketSpeed = 15
gravity = .7
rocketAngleSpeed = 0.3
cometMin = 10
cometMax = 25
thetaMinDeg = 30
thetaMaxDeg = 45
minCometVel = 2
maxCometVel = 6
maxComets = 3
size = Vector(400,400)
width = size.x
height = size.y

thetaMin = thetaMinDeg*math.pi/180
thetaMax = thetaMaxDeg*math.pi/180

cometPotPos = []
for position in range(width + 2*cometSize):
  cometPotPos.append(Vector(position-cometSize,-cometSize)) #top
  cometPotPos.append(Vector(position-cometSize,width+cometSize)) #bottom
for position in range(height + 2*cometSize):
  cometPotPos.append(Vector(-cometSize,position-cometSize)) #left
  cometPotPos.append(Vector(width+cometSize,position-cometSize)) #right

class Oorbitz(PycadeGame):
  @staticmethod
  def get_name():
    return "Oorbitz"

  def start(self):
    #variables local to Oorbitz
    global OorbitzLives
    global OorbitzScore
    OorbitzLives = 3
    OorbitzScore = 0
    self.isOver = False
    self.cometGroup = CometHolder()

    self.planet = Planet()
    self.rocket = Rocket()
    for comets in range(maxComets):
      self.cometGroup.createComet(self.planet)

  def update(self):
    if Action.LEFT in self.currentActions and not self.rocket.getLaunchStatus():
      self.rocket.addRocketAngle(rocketAngleSpeed)
    if Action.RIGHT in self.currentActions and not self.rocket.getLaunchStatus():
      self.rocket.addRocketAngle(-rocketAngleSpeed)
    if Action.BUTTON_1 in self.currentActions:
        self.rocket.setLaunchStatus(True)
    
    # delete rocket when out of bounds
    if self.rocket.isOutofBounds(self.rocket.pos,-2*cometSize, width + 2*cometSize, -2*cometSize, height + 2*cometSize):
      self.rocket.setLaunchStatus(False)
    #updating rocket and comet positions
    self.rocket.updateRocket()
    self.cometGroup.updateCometGroup(self.planet,self.rocket.pos,self.rocket.launched)

    if OorbitzLives <=0:
      self.lose()
      
    return True #len(self.currentActions) > 0 

  def draw(self):
    if self.isOver:
      self.drawText("YOU SUCK", Vector(10, 10))
      self.drawText(f'Score Was {OorbitzScore}', Vector(10, 50))
      return
    #draw background
    self.drawRect(BLACK,Vector(0,0), self.screenSize, 0)
    #draw planet
    self.drawCircle(BLUE, self.planet.pos, self.planet.size)
    #draw comets
    self.cometGroup.drawComets(self)
    self.drawCircle(RED, self.rocket.pos, rocketSize)
    #draw text
    self.drawText("Score", Vector(20,10))
    self.drawText(str(OorbitzScore), Vector(20,40))
    self.drawText("Lives", Vector(width-130,10))
    self.drawText(str(OorbitzLives), Vector(width-80,40))

  def lose(self):
    self.isOver = True

class Planet():
  def __init__(self):
    self.size = planetSize
    self.pos = Vector(width/2,height/2)
    self.vel = Vector(0,0)

  def movePlanet(self):
    pass

class Comet():
  def __init__(self, planet, size = None, pos = None, vel = None):
    if size and pos and vel:
      self.size = size
      self.pos = pos
      self.vel = vel
    else:
      self.pos = random.choice(cometPotPos)
      self.size = random.randrange(cometMin,cometMax)
      self.distance = math.sqrt((self.pos.x - planet.pos.x)**2 + (self.pos.y - planet.pos.y)**2)
      self.vel = Vector((planet.pos.x - self.pos.x),(planet.pos.y-self.pos.y)).scalarMultiply(1/self.distance)
      theta = random.choice([random.randrange(round(-thetaMax*10),round(-thetaMin*10))/10,random.randrange(round(thetaMin*10),round(thetaMax*10))/10]) 

      #applying random rotation of initial velocity
      self.vel.x = self.vel.x*math.cos(theta) - self.vel.y*math.sin(theta)
      self.vel.y = self.vel.x*math.sin(theta) + self.vel.y*math.cos(theta)
      self.vel = self.vel.scalarMultiply(random.randrange(minCometVel,maxCometVel)) #+round(OorbitzScore/500)))

class Rocket():
  def __init__(self):
    self.launched = False
    self.size = rocketSize
    self.rocketAngle = 90*math.pi/180
    self.pos = Vector(width/2 + planetSize*math.cos(self.rocketAngle), height/2 - planetSize*math.sin(self.rocketAngle))
    self.vel = Vector(0,0)
    
  def isOutofBounds(self, pos: Vector,minX,maxX,minY,maxY):
    return pos.x < minX or pos.x > maxX or pos.y < minY or pos.y > maxY

  def updateRocket(self):
    if self.launched:
      #launching rocket by adding rocket vel
      self.vel = Vector(math.cos(self.rocketAngle)*rocketSpeed,-math.sin(self.rocketAngle)*rocketSpeed)
      self.pos = self.pos.add(self.vel)
    else:
      #angle rocket along planet surface
      self.pos = Vector(width/2 + planetSize*math.cos(self.rocketAngle), height/2 - planetSize*math.sin(self.rocketAngle))

  def addRocketAngle(self,speed):
    self.rocketAngle += speed

  def getLaunchStatus(self):
    return self.launched

  def setLaunchStatus(self,status: bool):
    self.launched = status

class CometHolder():
  def __init__(self):
    self.comets = []
  def createComet(self,plt):
    self.comets.append(Comet(plt))
  def deleteComet(self):
    pass

  def sphereCollision(self, sphere1: Vector, radius1: int, sphere2: Vector, radius2: int):
    return (sphere1.x - sphere2.x)**2 + (sphere1.y - sphere2.y)**2 < (radius1 + radius2)**2
  
  def isOutofBounds(self, pos: Vector,minX,maxX,minY,maxY):
    return pos.x < minX or pos.x > maxX or pos.y < minY or pos.y > maxY

  def applyGravity(self, moon, planet):
    self.gravRadius = math.sqrt((moon.pos.x - planet.pos.x)**2 + (moon.pos.y - planet.pos.y)**2)
    gravMag = gravity/self.gravRadius**2 * planet.size**2
    gravNormal = planet.pos.sub(moon.pos).scalarMultiply(1/self.gravRadius)
    deltaV = gravNormal.scalarMultiply(gravMag)
    moon.vel = moon.vel.add(deltaV)
    moon.pos = moon.pos.add(moon.vel)
  
  def drawComets(self,Oorbitz:Oorbitz):
    for idx in range(len(self.comets)):
      Oorbitz.drawCircle(ORANGE,self.comets[idx].pos,self.comets[idx].size)
  
  def updateCometGroup(self,plt,rockPos,rockLaunched):
    global OorbitzLives
    global OorbitzScore

    #delete rocket when out of bounds
    if self.isOutofBounds(rockPos,-2*cometSize, width + 2*cometSize, -2*cometSize, height + 2*cometSize):
      self.rocketLaunched = False

    cgCopy = self.comets
    for i in range(len(cgCopy)):
      shouldRemove = False
      #delete comet if out of bounds
      if self.isOutofBounds(cgCopy[i].pos,-2*cometSize, width + 2*cometSize, -2*cometSize, height + 2*cometSize):
        shouldRemove = True
      #lose life if comet hits planet or hits rocket before launch
      if self.sphereCollision(plt.pos, plt.size, cgCopy[i].pos, cgCopy[i].size) or  (self.sphereCollision(rockPos, rocketSize, cgCopy[i].pos, cgCopy[i].size) and not rockLaunched):
        shouldRemove = True
        OorbitzLives -=1
      #if rocket hits comet
      if self.sphereCollision(rockPos, rocketSize, cgCopy[i].pos, cgCopy[i].size):
        shouldRemove = True
        OorbitzScore += round(self.gravRadius/10)*10
    
      for j in range(len(cgCopy)):
        if j == i:
          continue
        #apply gravity for all combinations of comets
        self.applyGravity(cgCopy[i], cgCopy[j])
        #combine comets if they collide
        if i > j and self.sphereCollision(cgCopy[i].pos, cgCopy[i].size, cgCopy[j].pos, cgCopy[j].size):
          #store squares of cgCopy i and j to variables
          newSize = math.sqrt(cgCopy[i].size**2 + cgCopy[j].size**2)
          newPos = cgCopy[i].pos.scalarMultiply(cgCopy[i].size**2/(cgCopy[i].size**2+cgCopy[j].size**2)).add(cgCopy[j].pos.scalarMultiply(cgCopy[j].size**2/(cgCopy[i].size**2+cgCopy[j].size**2)))
          newVel = cgCopy[i].vel.scalarMultiply(cgCopy[i].size**2/(cgCopy[i].size**2+cgCopy[j].size**2)).add(cgCopy[j].vel.scalarMultiply(cgCopy[j].size**2/(cgCopy[i].size**2+cgCopy[j].size**2)))
          self.comets.remove(cgCopy[i])
          self.comets.remove(cgCopy[j])
          self.comets.append(Comet(plt,newSize,newPos,newVel))
          self.comets.append(Comet(plt))
      if shouldRemove:
        self.comets.remove(cgCopy[i])
        self.comets.append(Comet(plt))
      self.applyGravity(cgCopy[i], plt)
    return self.comets