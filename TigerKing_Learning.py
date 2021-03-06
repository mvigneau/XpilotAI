### Final Project -- Mathieu Vigneault, Mahdia Qadid ###
### Date: 05-01-2020 ###
### Rabbit is a smart offensive agent that utilize a GA to learn and get smarter ###
### This program uses a genetic algorithm to evolve the agent's production system ###
### This is a file that will make the agent learn over time ### 

import libpyAI as ai
import statistics 
from Learning_Data import * 
from TigerKing_GA import * 

### Setting Up GA --- Important Parameters ###
population_size = 64
crossover_prob = 0.7
mutation_prob = 0.01
chromosome_size = 32
### Initialize the Population ###
##Order of chromosome do not matter when created ##
population = init_population(population_size, chromosome_size)
count_frame = 0
loop = 0
boolean = False
fitness_list = []
score = 0
generation_size = 200
generation = 1
first_time = True
done_learning = False

def AI_loop():
  global count_frame, loop, boolean, score, population_size, chromosome_size, population, mutation_prob, crossover_prob, fitness_list, generation, generation_size, first_time, done_learning
  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)

  ## Get A Chromosome in the Population -- Eventually Will go through each individual in the population ##
  current_chromosome = population[loop]
  
  ## Transform Each Gene insisde A Single Selected Chromosome. 0s & 1s Are Turned Into Intergers For Fuzzy Sets to understand ## 
  ## Each Value obtained is used to calculate the risk of each 45 degree around the agent ##
  ## Each value has its own "jump" variable which refers to the distance from each possible points/values ##
  ## The start and end represents the possible start point and end point for each variable and they depend on
  ## what the variiable is. It is to ensure a viable fuzzy set and fuzzy functions that these restrictions are applied. ##
  frontAlert = current_chromosome[0:5]
  frontAlertValue = transform(frontAlert, 25)
  
  backAlert = current_chromosome[5:9]
  backAlertValue = transform(backAlert, 25)
  
  speedAlert = current_chromosome[9:13]                 #4 bits
  speedAlertValue = transform(speedAlert, 1)            #1 jumps per value
  
  EnemyAlert = current_chromosome[13:18]                #5 bits
  EnemyAlertValue = transform(EnemyAlert, 50)           #50 jumps per value
  
  TrackSlowAlert = current_chromosome[18:22]            #4 bits
  TrackSlowAlertValue = transform(TrackSlowAlert, 25)   #25 jumps per value
  
  TrackFastAlert = current_chromosome[22:26]            #4 bits 
  TrackFastAlertValue = transform(TrackFastAlert, 25)   #25 jumps per value
  
  BulletAlert = current_chromosome[26:32]               #4 bits 
  BulletAlertValue = transform(BulletAlert, 15)         #15 jumps per value


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

  ## If the Enemy is Dead ##
  if(ai.selfAlive() == 0 and boolean == False): 

    ## Calculate Fitness Current Population ##
    score_previous = score
    score_current = ai.selfScore()
    fitness_value = fitness(population, count_frame, score_previous, score_current)
    fitness_list.append(fitness_value)

    ## If it went through the whole population and ready to move to next generation ##
    if((loop+1) == population_size):
      ## Output the fitness of population to allow user to see if learning is happening ##
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
      first_time = Save_Data("Tiger_Training_Data.xls", 0, titles, data, first_time)

      ## Select Next Generation -- Apply Crossover & Mutation ##
      new_population = select(population, fitness_list)
      new_population = crossover(new_population, chromosome_size, population_size, crossover_prob)
      new_population = mutate(new_population, chromosome_size, mutation_prob)
      population = new_population
      
      loop = 0
      count_frame = 0
      generation += 1
      fitness_list.clear()
  
      ### DONE -- QUIT ###
      if (generation == generation_size):
        quitAI()
 
    ## Move to the next individual in population ## 
    else:   
      loop += 1 
      count_frame = 0
    boolean = True


  else:

    ## The agent is Alive ##
    if(ai.selfAlive() == 1):
      
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

      count_frame += 3
      boolean = False

## Disabling the Game User Interface ##
ai.headlessMode()
## Starting the Game and the Agent ##
ai.start(AI_loop,["-name","Tiger_King","-join","localhost"])

#-join 136.244.227.81 -port 15351
  
