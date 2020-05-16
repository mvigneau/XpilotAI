### Final Project -- Mathieu Vigneault, Mahdia Qadid ###
### Date: 05-01-2020 ###
### Rabbit is a smart defensive agent that utilize a GA to learn and get smarter ###
### This program uses a genetic algorithm to evolve the agent's production system ###
### This is a the optimal agent after some learning against xpilot agent was done ###

import libpyAI as ai
import statistics 

frontAlertValue = 275
backAlertValue = 225
speedAlertValue = 1
EnemyAlertValue = 1300
TrackSlowAlertValue = 125
TrackFastAlertValue = 125
BulletAlertValue = 45

def AI_loop():
 
  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)

  ## Get values of variables for Wall Feelers, Head & Tracking ##
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
  
  ####### Getters Variable Regarding Important Information About Enemies ########
  ##Find the closest ennemy##
  enemy = ai.lockClose()
  ## Get the lockheadingdeg of enemy ##
  head = ai.lockHeadingDeg()
  ## Get the dstance from enemy ##
  enemyDist = ai.selfLockDist()

  ##### Production System Rules ######
  ### Turning Rules ###  
  if frontWall <= frontAlertValue and (left45Wall < right45Wall) and ai.selfSpeed() > speedAlertValue: 
    ai.turnRight(1)
  elif frontWall <= frontAlertValue and (left45Wall > right45Wall) and ai.selfSpeed() > speedAlertValue:
    ai.turnLeft(1)
  elif left90Wall <= frontAlertValue and ai.selfSpeed() > speedAlertValue:
    ai.turnRight(1) 
  elif right90Wall <= frontAlertValue and ai.selfSpeed() > speedAlertValue:
    ai.turnLeft(1)
  ### Thrust commands ####
  elif ai.selfSpeed() <= speedAlertValue and (frontWall >= frontAlertValue) and (left45Wall >= frontAlertValue) and (right45Wall >= frontAlertValue) and (right90Wall >= frontAlertValue) and (left90Wall >= frontAlertValue) and (left135Wall >= backAlertValue) and (right135Wall >= backAlertValue) and (backWall >= backAlertValue):
    ai.thrust(1)
  elif trackWall <= TrackFastAlertValue and ai.selfSpeed() >= speedAlertValue:
    ai.thrust(1)
  elif trackWall <= TrackSlowAlertValue and ai.selfSpeed() <= speedAlertValue:
    ai.thrust(1)
  elif backWall <= TrackFastAlertValue and ai.selfSpeed() >= speedAlertValue:
    ai.thrust(1)
  elif backWall <= TrackSlowAlertValue and ai.selfSpeed() <= speedAlertValue:
    ai.thrust(1)  
  elif left135Wall <= TrackFastAlertValue and ai.selfSpeed() >= speedAlertValue:
    ai.thrust(1)
  elif left135Wall <= TrackSlowAlertValue and ai.selfSpeed() <= speedAlertValue:
    ai.thrust(1)
  elif right135Wall <= TrackFastAlertValue and ai.selfSpeed() >= speedAlertValue:
    ai.thrust(1)
  elif right135Wall <= TrackSlowAlertValue and ai.selfSpeed() <= speedAlertValue:
    ai.thrust(1)
  ##### Bullet Avoidance Commands #####
  elif ai.shotAlert(0) >= 0 and ai.shotAlert(0) <= BulletAlertValue:
    if ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() <= speedAlertValue:
      ai.turnLeft(1)
      ai.thrust(1)
    elif ai.angleDiff(heading, ai.shotVelDir(0)) < 0 and ai.selfSpeed() <= speedAlertValue: 
      ai.turnRight(1)
      ai.thrust(1)
    elif ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() > speedAlertValue:
      ai.turnLeft(1)
    else:
      ai.turnRight(1)
  ##### Shooting Ennemy Commands #####
  elif enemyDist <= EnemyAlertValue and heading > (head) and ai.selfSpeed() > speedAlertValue:
    ai.turnRight(1)
    ai.fireShot()
  elif enemyDist <= EnemyAlertValue and heading < (head) and ai.selfSpeed() > speedAlertValue:
    ai.turnLeft(1)
    ai.fireShot()
  elif ai.selfSpeed() < speedAlertValue:
    ai.thrust(1)
  else:
    ai.thrust(0)


## Disabling the Game User Interface ##
## ai.headlessMode()
## Starting the Game and the Agent ##
ai.start(AI_loop,["-name","Rabbit","-join", "localhost"])
  
