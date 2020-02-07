### Program 1 -- Mathieu Vigneault,  
import libpyAI as ai
def AI_loop():
  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)
  #Set variables
  heading = int(ai.selfHeadingDeg())
  tracking = int(ai.selfTrackingDeg())
  frontWall = ai.wallFeeler(500,heading)
  left45Wall = ai.wallFeeler(500,heading+45)
  right45Wall = ai.wallFeeler(500,heading-45)
  left90Wall = ai.wallFeeler(500,heading+90)
  right90Wall = ai.wallFeeler(500,heading-90)
  left135Wall = ai.wallFeeler(500,heading+135)
  right135Wall = ai.wallFeeler(500,heading-135)
  backWall = ai.wallFeeler(500,heading-180) 
  trackWall = ai.wallFeeler(500,tracking)
  
  
  #######   Shooting Ennemies  ########
  ##Find the closest ennemy##
  ClosestID = ai.closestShipId()
  #print(ClosestID)
  ##Get the closest ennemy direction and speed##
  ClosestSpeed = ai.enemySpeedId(ClosestID)
  #print(ClosestSpeed)
  ClosestDir = ai.enemyTrackingDegId(ClosestID)
  #print(ClosestDir)
  ## Get the lockheadingdeg ##
  enemy = ai.lockNext()
  print(enemy)
  head = ai.lockHeadingDeg()
  print(head)
  enemyDist = ai.selfLockDist()
  print(enemyDist)
  
  #Thrust rules
  if ai.selfSpeed() <= 10 and (frontWall >= 200) and (left45Wall >= 200) and (right45Wall >= 200) and (right90Wall >= 200) and (left90Wall >= 200) and (left135Wall >= 50) and (right135Wall >= 50) and (backWall >= 50):
    print("go forward")
    ai.thrust(1)
  elif trackWall < 75:
    ai.thrust(1)
  elif frontWall <= 300 and (left45Wall < right45Wall): 
    print("turning right")
    ai.turnRight(1)
  elif left90Wall <= 200:
    print("turning right")
    ai.turnRight(1) 
  elif frontWall <= 300 and (left45Wall > right45Wall):
    ai.turnLeft(1)
  elif right90Wall <= 200:
    #print("turning left")
    ai.turnLeft(1)
  elif backWall <= 40 or left135Wall <= 40 or right135Wall <= 40:
    ai.thrust(1)  
  elif enemyDist <= 500 and heading > head:
    ai.turnRight(1)
    ai.fireShot()
  elif enemyDist <= 500 and heading < head:
    ai.turnLeft(1)
    ai.fireShot()
  else:
    print("chilling")
    ai.thrust(0)
  
  #######   Shooting Ennemies  ########
  ##Find the closest ennemy##
  ClosestID = ai.closestShipId()
  #print(ClosestID)
  ##Get the closest ennemy direction and speed##
  ClosestSpeed = ai.enemySpeedId(ClosestID)
  #print(ClosestSpeed)
  ClosestDir = ai.enemyTrackingDegId(ClosestID)
  #print(ClosestDir)
  ## Get the lockheadingdeg ##
  enemy = ai.lockNext()
  print(enemy)
  head = ai.lockHeadingDeg()
  print(head)
  enemyDist = ai.selfLockDist()
  print(enemyDist)
  

ai.start(AI_loop,["-name","Dubster","-join","localhost"])
