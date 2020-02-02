#Evan Gray - January 2018
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
  
  #Thrust rules
  if ai.selfSpeed() <= 5 and (frontWall >= 200) and (left45Wall >= 200) and (right45Wall >= 200) and (right90Wall >= 200) and (left90Wall >= 200) and (left135Wall >= 50) and (right135Wall >= 50) and (backWall >= 50):
    ai.thrust(1)
  elif trackWall < 100:
    ai.thrust(1)
  elif frontWall <= 300 and (left45Wall < right45Wall): 
    ai.turnRight(1)
  elif left90Wall <= 200:
    ai.turnRight(1) 
  elif frontWall <= 300 and (left45Wall > right45Wall):
    ai.turnLeft(1)
  elif right90Wall <= 200:
    ai.turnLeft(1)
  elif backWall <= 30 or left135Wall <= 30 or right135Wall <= 30:
    ai.thrust(1)
  else:
    ai.thrust(0)
   
  #Ennemy shooting rules
  #find closest ennemy 
  ClosestID = closestShipId()
  #get closest ennemy speed and direction
  ClosestSpeed = ennemySpeedId(ClosestID)
  ClosestDirection = enemyTrackingDegId(ClosestID) 
  
  ai.fireShot()

ai.start(AI_loop,["-name","Dubster","-join","localhost"])
