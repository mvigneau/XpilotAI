### Program 2 -- Mathieu Vigneault, ______ ###
### Date: 02-14-2020 ###
### This program uses fuzzy rules to determine the wall avoidance ###
import libpyAI as ai
import statistics 
from Dumpster_Fuzzy import *
from Dumpster_GA import *

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
  global count_frame, loop, boolean, score, generation, generation_size, first_time, done_learning
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
      print("Best Fitness:", max(fitness_list))
      
      ## Finding the optimal chromosome to output it in data file ##
      string_maxChromosome = ""
      for chrom_max in range(chromosome_size):
         string_maxChromosome = string_maxChromosome + str(population[fitness_list.index(max(fitness_list))][chrom_max])

      ## Formatting entire population in a big string to register it in excel file##
      string_population = ""
      for pop in range(population_size):
        for pop_chrom in range(chromosome_size):
          string_population = string_population + str(population[pop][pop_chrom])
        if(pop != (population_size-1)):
          string_population = string_population + ","

      ## Formatting entire population's fitness in a big string to register it in excel file##
      string_fitness = ""
      for fit in range(len(fitness_list)):
        string_fitness = string_fitness + str(fitness_list[fit])
        if(fit != (len(fitness_list)-1)):
          string_fitness = string_fitness + ","


      ## Output Data into Excel File ##
      titles = ["Generation", "Average Fitness", "Best Fitness","Population Size", "Chromosome Size", "Crossover Probability", "Mutation Probability", "Best Chromosome", "Entire Population Chromosome", "Entire Population Fitness"]
      data = [generation, statistics.mean(fitness_list), max(fitness_list), population_size, chromosome_size, crossover_prob, mutation_prob, string_maxChromosome, string_population, string_fitness]
      first_time = Save_Data("Dumpster_Training_Data.xls", 0, titles, data, first_time)

      ## Select Population For Next Generation -- Apply Crossover & Mutation ##
      new_population = select(population, fitness_list)
      new_population = crossover(new_population, chromosome_size, population_size, crossover_prob)
      new_population = mutate(new_population, chromosome_size, mutation_prob)
      population = new_population

      loop = 0
      count_frame = 0
      generation += 1
      fitness_list.clear()
      
      ### DONE -- QUIT ###
      if(generation == generation_size):
        print("Done")
        quitAI()

    else:   
      loop += 1 
      count_frame = 0
    boolean = True

  ### Rules ###
  else:

    if(ai.selfAlive() == 1):
      # print("Alive")

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
        if(ai.shotVelDir(0) != -1  and ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() <= 5):
          ai.turnLeft(1)
          ai.thrust(1)
          #print("Rule 5")
        elif(ai.shotVelDir(0) != -1 and ai.angleDiff(heading, ai.shotVelDir(0)) < 0 and ai.selfSpeed() <= 5): 
          ai.turnRight(1)
          ai.thrust(1)
          #print("Rule 6")
        elif(ai.shotVelDir(0) != -1 and ai.angleDiff(heading, ai.shotVelDir(0)) > 0 and ai.selfSpeed() > 5):
          ai.turnLeft(1)
          #print("Rule 7")
        else:
          ai.turnRight(1)
          #print("Rule 8")
        ##### Shooting Ennemy Commands #####
      elif(enemyDist <= 3000 and heading > (head) and enemyDist != 0 and ai.selfSpeed() > 5):
        #print("Rule 9")
        ai.turnRight(1)
        ai.fireShot()
      elif(enemyDist <= 3000 and heading < (head) and enemyDist != 0 and ai.selfSpeed() > 5):
        #print("Rule 10")
        ai.turnLeft(1)
        ai.fireShot()
      elif(ai.selfSpeed() < 5):
        #print("Rule 11")
        ai.thrust(1)
      else:
        #print("Rule 12")
        ai.thrust(0)

      count_frame += 3
      boolean = False
      #print("nothing")
      

#ai.headlessMode()
ai.start(AI_loop,["-name", "Dumpster", "-join", "localhost"])

#ai.start(AI_loop,["-name", "Dumpster", "-join", "136.244.227.81", "-port", "15350"])
