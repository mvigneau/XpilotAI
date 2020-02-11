### Program 2 -- Mathieu Vigneault, 
import libpyAI as ai
from Program2_Fuzzy import *
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
  
  result_list = []
  for i in range(8):
    Degree = tracking+(45*i)
    Speed = ai.selfSpeed()
    Distance = ai.wallFeeler(1000,tracking+(45*i))
    result = Closing_Rate(Degree, tracking, Speed, Distance)
    result_list.append(result)
  	
    ### Fuzzy membership ###
    closing_rate, distance = Closing_Rate(Degree, tracking, Speed, Distance)
    a = Fuzzy(closing_rate,distance)
	
  print(result_list)
  
  #print(tracking)
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
  #print(enemy)
  head = ai.lockHeadingDeg()
  #print(head)
  enemyDist = ai.selfLockDist()
  #print(enemyDist)
  
  ### Turning Rules ###
  if frontWall <= 200 and (left45Wall < right45Wall): 
    #print("turning right")
    ai.turnRight(1)
  elif frontWall <= 200 and (left45Wall > right45Wall):
    ai.turnLeft(1)
  elif left90Wall <= 200:
    #print("turning right")
    ai.turnRight(1) 
  elif right90Wall <= 200:
    #print("turning left")
    ai.turnLeft(1)
  ### Thrust commands ####
  elif ai.selfSpeed() <= 10 and (frontWall >= 200) and (left45Wall >= 200) and (right45Wall >= 200) and (right90Wall >= 200) and (left90Wall >= 200) and (left135Wall >= 50) and (right135Wall >= 50) and (backWall >= 50):
    #print("go forward")
    ai.thrust(1)
  elif trackWall < 75 and ai.selfSpeed() >= 10:
    ai.thrust(1)
  elif trackWall < 50 and ai.selfSpeed() <= 10:
    ai.thrust(1)
  elif backWall <= 75:
    ai.thrust(1)  
  elif left135Wall <= 75:
    ai.thrust(1)
  elif right135Wall <= 75:
    ai.thrust(1)
  ##### Shooting Ennemy Commands #####
  elif enemyDist <= 500 and heading > (head):
    ai.turnRight(1)
    ai.fireShot()
  elif enemyDist <= 500 and heading < (head):
    ai.turnLeft(1)
    ai.fireShot()
  else:
    #print("chilling")
    ai.thrust(0)
  
  

ai.start(AI_loop,["-name","Dubster","-join","localhost"])
