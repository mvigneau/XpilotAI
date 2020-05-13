### Program 1 -- Mathieu Vigneault,  
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
  global count_frame, loop, boolean, score, population_size, chromosome_size, population, mutation_prob, crossover_prob, fitness_list, generation, generation_size, first_time, done_learning
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
  #print(enemy)
  head = ai.lockHeadingDeg()
  #print(head)
  enemyDist = ai.selfLockDist()
  #print(enemyDist)
  #print(count_frame)

  ## Production System Rules ##    
  if frontWall <= frontAlertValue and (left45Wall < right45Wall) and ai.selfSpeed() > speedAlertValue: 
    #print("turning right")
    ai.turnRight(1)
  elif frontWall <= frontAlertValue and (left45Wall > right45Wall) and ai.selfSpeed() > speedAlertValue:
    ai.turnLeft(1)
  elif left90Wall <= frontAlertValue and ai.selfSpeed() > speedAlertValue:
    #print("turning right")
    ai.turnRight(1) 
  elif right90Wall <= frontAlertValue and ai.selfSpeed() > speedAlertValue:
    #print("turning left")
    ai.turnLeft(1)
  ### Thrust commands ####
  elif ai.selfSpeed() <= speedAlertValue and (frontWall >= frontAlertValue) and (left45Wall >= frontAlertValue) and (right45Wall >= frontAlertValue) and (right90Wall >= frontAlertValue) and (left90Wall >= frontAlertValue) and (left135Wall >= backAlertValue) and (right135Wall >= backAlertValue) and (backWall >= backAlertValue):
    #print("go forward")
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
    #print("chilling")
    ai.thrust(0)


#ai.headlessMode()
ai.start(AI_loop,["-name","Rabbit","-join", "localhost"])

##-join 136.244.227.80 -port 15351
  
