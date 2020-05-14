### Program 2 -- Mathieu Vigneault, ______ ###
### Date: 02-14-2020 ###
### This program uses fuzzy rules to determine the wall avoidance ###
import libpyAI as ai
import statistics 
from Dumpster_Fuzzy import *

closingRate_SlowTopAlertValue = 0
closingRate_MediumTopLeftAlertValue = 9
closingRate_MediumTopRightAlertValue = 21
closingRate_FastTopAlertValue = 27 
closingRate_SlowBottomAlertValue = 6
closingRate_MediumBottomLeftAlertValue = 0
closingRate_MediumBottomRightAlertValue = 31
closingRate_FastBottomAlertValue = 15
Distance_CloseTopAlertValue = 950
Distance_FarTopAlertValue = 2250
Distance_CloseBottomAlertValue = 1701
Distance_FarBottomAlertValue = 1250

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
    low, medium, fast = Fuzzy_Speed(closing_rate, closingRate_SlowTopAlertValue, closingRate_SlowBottomAlertValue, closingRate_MediumBottomLeftAlertValue, closingRate_MediumTopLeftAlertValue, closingRate_MediumTopRightAlertValue, closingRate_MediumBottomRightAlertValue, closingRate_FastBottomAlertValue, closingRate_FastTopAlertValue)
    #print("low-med-fast", low, medium, fast)
    close, far = Fuzzy_Distance(distance, Distance_CloseTopAlertValue, Distance_CloseBottomAlertValue, Distance_FarBottomAlertValue, Distance_FarTopAlertValue)
    #print("close-far", close, far)
    risk = Fuzzy_Risk(low, medium, fast, close, far)
    risk_list.append(risk)

  ## Get the direction in deg that is most risky for the robot ##
  max_risk = max(risk_list)
  track_risk = (tracking + (risk_list.index(max_risk)*45) % 360)
  min_risk = min(risk_list)
  
  # print("found max risk", max_risk)

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
  enemy = ai.lockClose()
  #print(enemy)
  head = ai.lockHeadingDeg()
  #print(head)
  enemyDist = ai.selfLockDist()
  
  # print("max_risk: ", max_risk)
  # print("track_risk: ", track_risk)
  # print("heading: ", heading)

  ## Get the angles on both side between tracking and heading ##
  dist = (heading - track_risk) % 360
  dist2 = (360 - dist) % 360
  # print("dist: ", dist)
  # print("dist2: ", dist2)
  
  ## Production system rules based off fuzzy output ##
  if(dist <= 130 and dist >= 0 and ai.selfSpeed() > 0 and max_risk >= 75):
    ai.turnLeft(1)
    #print("Rule 1")
  elif(dist2 <= 130 and dist2 >= 0 and ai.selfSpeed() > 0 and max_risk >= 75):
    ai.turnRight(1)
    #print("Rule 2")
  elif(ai.selfSpeed() <= 10):
    ai.thrust(1)
    #print("Rule 3")
  elif(trackWall <= 150):
    ai.thrust(1)
    #print("Rule 4")
    ##### Bullet Avoidance Commands #####
  elif(ai.shotAlert(0) >= 0 and ai.shotAlert(0) <= 50):
    #print("YES")
    if(ai.shotVelDir(0) != -1  and ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() <= 3):
      ai.turnLeft(1)
      ai.thrust(1)
      #print("Rule 5")
    elif(ai.shotVelDir(0) != -1 and ai.angleDiff(heading, ai.shotVelDir(0)) < 0 and ai.selfSpeed() <= 3): 
      ai.turnRight(1)
      ai.thrust(1)
      #print("Rule 6")
    elif(ai.shotVelDir(0) != -1 and ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() > 3):
      ai.turnLeft(1)
      #print("Rule 7")
    else:
      ai.turnRight(1)
      #print("Rule 8")
    ##### Shooting Ennemy Commands #####
  elif(enemyDist <= 100000 and heading > (head) and ai.selfSpeed() > 3):
    #print("Rule 9")
    ai.turnRight(1)
    ai.fireShot()
  elif(enemyDist <= 100000 and heading < (head) and ai.selfSpeed() > 3):
    #print("Rule 10")
    ai.turnLeft(1)
    ai.fireShot()
  elif(ai.selfSpeed() < 5):
    #print("Rule 11")
    ai.thrust(1)
  else:
    #print("Rule 12")
    ai.thrust(0)
  

#ai.headlessMode()
ai.start(AI_loop,["-name", "Dumpster", "-join", "localhost"])

#ai.start(AI_loop,["-name", "Dumpster", "-join", "136.244.227.81", "-port", "15350"])
