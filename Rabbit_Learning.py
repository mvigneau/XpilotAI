### Program 1 -- Mathieu Vigneault,  
import libpyAI as ai
import statistics 
from Rabbit_GA import * 

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
  global count_frame, loop, boolean, score, population_size, chromosome_size, population, mutation_prob, crossover_prob, fitness_list, generation, generation_size
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
  if(ai.selfAlive() == 0 and boolean == False): 

    ## Calculate Fitness Current Population ##
    score_previous = score
    score_current = ai.selfScore()
    fitness_value = fitness(population, count_frame, score_previous, score_current)
    fitness_list.append(fitness_value)
    generation += 1

    if((loop+1) == population_size):
      print("Generation:", generation)
      print("Agent Fitness:", fitness_list)
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
      fitness_list.clear()
      if generation == generation_size:
        print("Done")
        ### DONE -- QUIT ###
      
    else:   
      loop += 1 
      count_frame = 0
    boolean = True

  ### Turning Rules ###
  else:

    if(ai.selfAlive() == 1):
      
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

      count_frame += 3
      boolean = False


    # count_frame += 1
  # else:
  #   print(count_frame)
# def main():
  ### Setting Up GA ###
  # population_size = 1
  # crossover_prob = 0.7
  # mutation_prob = 0.01
  # chromosome_size = 13
  # fitness_target = 20
  # population = init_population(population_size, chromosome_size)
  # count_frame = 0
  # ai.start(AI_loop,["-name","Rabbit","-join","localhost"])

ai.headlessMode()
ai.start(AI_loop,["-name","Rabbit","-join","localhost"])


  
