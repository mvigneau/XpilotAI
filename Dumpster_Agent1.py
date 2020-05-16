### Final Project -- Mathieu Vigneault, Mahdia Qadid ###
### Date: 05-01-2020 ###
### This program uses fuzzy rules to determine the wall avoidance and a genetic algorithm to evolve the fuzzy rules ###
### This is a the optimal agent after some learning against xpilot agent was done ###

import libpyAI as ai
import statistics 
from Dumpster_Fuzzy import *

## Optimal Agent Fuzzy Sets Values ##
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

  #Set variables for Wall feelers, heading and tracking of the agent ##
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
  
  ## Create an array that represents the closing rate of each 45 degree of the full 360 degrees surrounding the agent ##
  result_list = []
  ## Array of the same size, but contains the risk of each direction ##
  risk_list = []
  for i in range(8):
    Degree = tracking+(45*i)
    Speed = ai.selfSpeed()
    Distance = ai.wallFeeler(10000,tracking+(45*i))
    result = Closing_Rate(Degree, tracking, Speed, Distance)
    result_list.append(result)

    ### Calculate the Fuzzy membership ###
    ### 1. Fuzzy Membership For Closing Rate (Speed + Tracking Involved) ###
    ### 2. Fuzzy Membership For Distance From Walls ###  
    closing_rate, distance = Closing_Rate(Degree, tracking, Speed, Distance)
    low, medium, fast = Fuzzy_Speed(closing_rate, closingRate_SlowTopAlertValue, closingRate_SlowBottomAlertValue, closingRate_MediumBottomLeftAlertValue, closingRate_MediumTopLeftAlertValue, closingRate_MediumTopRightAlertValue, closingRate_MediumBottomRightAlertValue, closingRate_FastBottomAlertValue, closingRate_FastTopAlertValue)
    close, far = Fuzzy_Distance(distance, Distance_CloseTopAlertValue, Distance_CloseBottomAlertValue, Distance_FarBottomAlertValue, Distance_FarTopAlertValue)
    #print("close-far", close, far)
    risk = Fuzzy_Risk(low, medium, fast, close, far)
    risk_list.append(risk)

  ## Get the direction in deg that is most risky for the robot as well as the least risky direction ##
  max_risk = max(risk_list)
  track_risk = (tracking + (risk_list.index(max_risk)*45) % 360)
  min_risk = min(risk_list) ## Note: Biase Towards Left Side since min get the first min when risk might be equal ##
  

  ####### Getters Variable Regarding Important Information About Enemies ########
  ##Find the closest ennemy##
  enemy = ai.lockClose()
  ## Get the lockheadingdeg of enemy ##
  head = ai.lockHeadingDeg()
  ## Get the dstance from enemy ##
  enemyDist = ai.selfLockDist()
  

  ## Get the angles on both side between tracking and heading to decide which way to turn ##
  dist = (heading - track_risk) % 360
  dist2 = (360 - dist) % 360

  ###### Production System Rules ######
  ## Turning Rules ##
  if(dist <= 130 and dist >= 0 and ai.selfSpeed() > 0 and max_risk >= 75):
    ai.turnLeft(1)
  elif(dist2 <= 130 and dist2 >= 0 and ai.selfSpeed() > 0 and max_risk >= 75):
    ai.turnRight(1)
  elif(trackWall <= 150):
    ai.thrust(1)
  ##### Bullet Avoidance Commands #####
  elif(ai.shotAlert(0) >= 0 and ai.shotAlert(0) <= 50):
    if(ai.shotVelDir(0) != -1  and ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() <= 5):
      ai.turnLeft(1)
      ai.thrust(1)
    elif(ai.shotVelDir(0) != -1 and ai.angleDiff(heading, ai.shotVelDir(0)) < 0 and ai.selfSpeed() <= 5): 
      ai.turnRight(1)
      ai.thrust(1)
    elif(ai.shotVelDir(0) != -1 and ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() > 5):
      ai.turnLeft(1)
    else:
      ai.turnRight(1)
  ##### Shooting Ennemy Commands #####
  elif(enemyDist <= 3000 and heading > (head) and enemyDist != 0 and ai.selfSpeed() > 2):
    ai.turnRight(1)
    ai.fireShot()
  elif(enemyDist <= 3000 and heading < (head) and enemyDist != 0 and ai.selfSpeed() > 2):
    ai.turnLeft(1)
    ai.fireShot()
  ## Rules if nothing is happening ##
  elif(ai.selfSpeed() < 5):
    ai.thrust(1)
  else:
    ai.thrust(0)

## Disabling the Game User Interface ##
#ai.headlessMode()
## Starting the Game and the Agent ##
ai.start(AI_loop,["-name", "Dumpster", "-join", "localhost"])
