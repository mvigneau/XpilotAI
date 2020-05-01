### Program 2 -- Mathieu Vigneault, ______ ###
### Date: 02-14-2020 ###
### This program uses fuzzy rules to determine the wall avoidance ###
import libpyAI as ai
from Dumpster_Fuzzy import *
from Dumpster_GA import *

### Setting Up GA ###
population_size = 2
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
  global count_frame, loop, boolean, score, population_size, chromosome_size, population, mutation_prob, crossover_prob, fitness_list, generation, generation_size
  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)

  ### Order of chromosome do not matter when created ###
  #print("pop", population)
  current_chromosome = population[loop]
  print(current_chromosome)
  
  closingRate_SlowTopAlert = current_chromosome[0:4]
  closingRate_SlowTopAlertValue = transform_fuzzy(closingRate_SlowTopAlert, 1, 0, 16) 
  print("closingRate_SlowTopAlertValue", closingRate_SlowTopAlertValue)
  closingRate_MediumTopLeftAlert = current_chromosome[4:8]                 
  closingRate_MediumTopLeftAlertValue = transform_fuzzy(closingRate_MediumTopLeftAlert, 1, closingRate_SlowTopAlertValue, closingRate_SlowTopAlertValue+16) 
  print("closingRate_MediumTopLeftAlertValue", closingRate_MediumTopLeftAlertValue)
  closingRate_MediumTopRightAlert = current_chromosome[8:12]                 
  closingRate_MediumTopRightAlertValue = transform_fuzzy(closingRate_MediumTopRightAlert, 1, closingRate_MediumTopLeftAlertValue, closingRate_MediumTopLeftAlertValue+16) 
  print("closingRate_MediumTopRightAlertValue", closingRate_MediumTopRightAlertValue)
  closingRate_FastTopAlert = current_chromosome[12:16]                 
  closingRate_FastTopAlertValue = transform_fuzzy(closingRate_FastTopAlert, 1, closingRate_MediumTopRightAlertValue, closingRate_MediumTopRightAlertValue+16) 
  
  #print("closingRate_FastTopAlertValue", closingRate_FastTopAlertValue)
  closingRate_SlowBottomAlert = current_chromosome[16:20]                               
  closingRate_SlowBottomAlertValue = transform_fuzzy(closingRate_SlowBottomAlert, 1, closingRate_SlowTopAlertValue, closingRate_FastTopAlertValue)   

  print("closingRate_SlowBottomAlertValue", closingRate_SlowBottomAlertValue)
  closingRate_MediumBottomLeftAlert = current_chromosome[20:24]                 
  closingRate_MediumBottomLeftAlertValue = transform_fuzzy(closingRate_MediumBottomLeftAlert, 1, 0, closingRate_MediumTopLeftAlertValue) 

  closingRate_MediumBottomRightAlert = current_chromosome[24:28]                 
  closingRate_MediumBottomRightAlertValue = transform_fuzzy(closingRate_MediumBottomRightAlert, 1, closingRate_MediumTopRightAlertValue, closingRate_MediumTopRightAlertValue+16) 
 
  closingRate_FastBottomAlert = current_chromosome[28:32]                 
  closingRate_FastBottomAlertValue = transform_fuzzy(closingRate_FastBottomAlert, 1, closingRate_SlowBottomAlertValue, closingRate_FastTopAlertValue) 
  print("closingRate_FastBottomAlertValue", closingRate_FastBottomAlertValue)



  Distance_CloseTopAlert = current_chromosome[32:37]
  Distance_CloseTopAlertValue = transform_fuzzy(Distance_CloseTopAlert, 50, 0, 16) 

  Distance_FarTopAlert = current_chromosome[37:42]
  Distance_FarTopAlertValue = transform_fuzzy(Distance_CloseTopAlert, 50, Distance_CloseTopAlertValue, Distance_CloseTopAlertValue+16) 

  Distance_CloseBottomAlert = current_chromosome[42:47]
  Distance_CloseBottomAlertValue = transform_fuzzy(Distance_CloseBottomAlert, 50, Distance_CloseTopAlertValue, Distance_FarTopAlertValue) 

  Distance_FarBottomAlert = current_chromosome[47:52]
  Distance_FarBottomAlertValue = transform_fuzzy(Distance_FarBottomAlert, 50, Distance_CloseBottomAlertValue, Distance_FarTopAlertValue) 

  print("got pass the chrom")

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
    print("low-med-fast", low, medium, fast)
    close, far = Fuzzy_Distance(distance)
    print("close-far", close, far)
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
  


  if(ai.selfAlive() == 0 and boolean == False): 

    ## Calculate Fitness Current Population ##
    score_previous = score
    score_current = ai.selfScore()
    fitness_value = fitness(population, count_frame, score_previous, score_current)
    fitness_list.append(fitness_value)

    if((loop+1) == population_size):
      print("Generation:", generation)
      print("Agent Fitness:")
      print(fitness_list)
      print("Average Fitness:", statistics.mean(fitness_list))
      ## Select Next Generation -- Apply Crossover & Mutation ##
      new_population = select(population, fitness_list)
      #print("new", new_population)
      new_population = crossover(new_population, chromosome_size, population_size, crossover_prob)
      #print("crossover", new_population)
      new_population = mutate(new_population, chromosome_size, mutation_prob)
      #print("mutate", new_population)
      population = new_population
      #print("population", population)
      loop = 0
      count_frame = 0
      generation += 1
      fitness_list.clear()
      if generation == generation_size:
        print("Done")
        ### DONE -- QUIT ###
      
    else:   
      loop += 1 
      count_frame = 0
    boolean = True

  ### Rules ###
  else:
    
    if(ai.selfAlive() == 1):
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

      count_frame += 3
      boolean = False
    
#ai.headlessMode()
ai.start(AI_loop,["-name", "Dumpster", "-join", "localhost"])

#ai.start(AI_loop,["-name", "Dumpster", "-join", "136.244.227.81", "-port", "15350"])
