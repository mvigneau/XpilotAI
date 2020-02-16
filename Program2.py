### Program 2 -- Mathieu Vigneault, ______ ###
### Date: 02-14-2020 ###
### This program uses fuzzy rules to determine the wall avoidance ###

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
  risk_list = []
  for i in range(8):
    Degree = tracking+(45*i)
    Speed = ai.selfSpeed()
    Distance = ai.wallFeeler(10000,tracking+(45*i))
    result = Closing_Rate(Degree, tracking, Speed, Distance)
    result_list.append(result)
  	
    ### Fuzzy membership ###
    closing_rate, distance = Closing_Rate(Degree, tracking, Speed, Distance)
    low, medium, fast = Fuzzy_Speed(closing_rate)
    close, far = Fuzzy_Distance(distance)
    risk = Fuzzy_Risk(low, medium, fast, close, far)
    risk_list.append(risk)
  
  ## Get the direction in deg that is most risky for the robot ##
  max_risk = max(risk_list)
  track_risk = (tracking + (risk_list.index(max_risk)*45) % 360)
  min_risk = min(risk_list)
  

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
  
  #print("max_risk: ", max_risk)
  #print("track_risk: ", track_risk)
  #print("heading: ", heading)
  
  ## Get the angles on both side between tracking and heading ##
  dist = (heading - track_risk) % 360
  dist2 = (360 - dist) % 360
  #print("dist: ", dist)
  #print("dist2: ", dist2)
  
  ## Production system rules based off fuzzy output ##
  if(dist <= 130 and dist >= 0 and ai.selfSpeed() > 0 and max_risk >= 40):
    ai.turnLeft(1)
    #print("turning left")
  elif(dist2 <= 130 and dist2 >= 0 and ai.selfSpeed() > 0 and max_risk >= 40):
    ai.turnRight(1)
    #print("turning right")
  elif(ai.selfSpeed() <= 10):
    ai.thrust(1)
    #print("thrust")
  elif(trackWall <= 150 and dist):
    ai.thrust(1)
    #print("thrust")
  elif enemyDist <= 500 and heading > (head) and enemyDist != 0:
    ai.turnRight(1)
    ai.fireShot()
  elif enemyDist <= 500 and heading < (head) and enemyDist != 0:
    ai.turnLeft(1)
    ai.fireShot()
  else:
    #print("chilling")
    ai.thrust(0)
    ai.fireShot()
  
  

ai.start(AI_loop,["-name","Dubster","-join","localhost"])
