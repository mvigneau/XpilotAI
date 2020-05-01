### Program 2 -- Mathieu Vigneault, ______ ###
### Date: 02-14-2020 ###
### This program uses fuzzy rules to determine the wall avoidance ###
import libpyAI as ai
from Dumbster_Fuzzy import *
from Dumbster_GA import *

### Setting Up GA ###
population_size = 32
crossover_prob = 0.7
mutation_prob = 0.01
chromosome_size = 26
fitness_target = 20
population = init_population(population_size, chromosome_size)
count_frame = 0
loop = 0
boolean = False
fitness_list = []
score = 0
generation_size = 200
generation = 0

def AI_loop():
  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)

  #print("pop", population)
  current_chromosome = population[loop]
  #print(current_chromosome)
  frontAlert = current_chromosome[0:5]
  #print("frontAlert", frontAlert)
  frontAlertValue = transform(frontAlert, 25)
  #print("frontAlertValue", frontAlertValue)
  backAlert = current_chromosome[5:9]
  backAlertValue = transform(backAlert, 25)
  #print("backAlertValue", backAlertValue)
  speedAlert = current_chromosome[9:13]                 #4 bits
  speedAlertValue = transform(speedAlert, 1)            #1 jumps per value
  #print("speedAlertValue", speedAlertValue)
  EnemyAlert = current_chromosome[13:18]                #5 bits
  EnemyAlertValue = transform(EnemyAlert, 50)           #50 jumps per value
  #print("speedAlertValue", speedAlertValue)
  TrackSlowAlert = current_chromosome[18:22]            #4 bits
  TrackSlowAlertValue = transform(TrackSlowAlert, 25)   #25 jumps per value
  #print("speedAlertValue", speedAlertValue)
  TrackFastAlert = current_chromosome[22:26]            #4 bits 
  TrackFastAlertValue = transform(TrackFastAlert, 25)   #25 jumps per value
  #print("speedAlertValue", speedAlertValue)


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
  enemy = ai.lockClose()
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
  if(dist <= 130 and dist >= 0 and ai.selfSpeed() > 0 and max_risk >= 75):
    ai.turnLeft(1)
    #print("turning left")
  elif(dist2 <= 130 and dist2 >= 0 and ai.selfSpeed() > 0 and max_risk >= 75):
    ai.turnRight(1)
    #print("turning right")
  elif(ai.selfSpeed() <= 10):
    ai.thrust(1)
    #print("thrust")
  elif(trackWall <= 150):
    ai.thrust(1)
    #print("thrust")
  elif(enemyDist <= 3000 and heading > (head) and enemyDist != 0):
    ai.turnRight(1)
    ai.fireShot()
  elif(enemyDist <= 3000 and heading < (head) and enemyDist != 0):
    ai.turnLeft(1)
    ai.fireShot()
  else:
    #print("chilling")
    ai.thrust(0)
    ai.fireShot()
  
  

ai.start(AI_loop,["-name", "Dubster", "-join", "136.244.227.81", "-port", "15350"])
