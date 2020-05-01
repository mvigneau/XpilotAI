### Program 1 -- Mathieu Vigneault,  
import libpyAI as ai
from Rabbit_GA import * 

### Setting Up GA ###
population_size = 4
crossover_prob = 0.7
mutation_prob = 0.01
chromosome_size = 13
fitness_target = 20
population = init_population(population_size, chromosome_size)
count_frame = 0
loop = 0
boolean = False
fitness_list = []
score = 0

def AI_loop():
  global count_frame, loop, boolean, score, population_size, population, mutation_prob
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
  speedAlert = current_chromosome[9:13]
  speedAlertValue = transform(speedAlert, 1)
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
  
  if(ai.selfAlive() == 0 and boolean == False): 

    ## Calculate Fitness Current Population ##
    score_previous = score
    score_current = ai.selfScore()
    fitness_value = fitness(population, count_frame, score_previous, score_current)
    fitness_list.append(fitness_value)

    if((loop+1) == population_size):
      print(fitness_list)
      ## Select Next Generation -- Apply Crossover & Mutation ##
      new_population = select(population, fitness_list)
      print"new", new_population)
      new_population = crossover(new_population, chromosome_size, population_size, crossover_prob)
      print("crossover", new_population)
      new_population = mutate(new_population, mutation_prob)
      print("mutate", new_population)
      population = new_population
      print("population", population)
      loop = 0
      count_frame = 0
      fitness_list.clear()
    else:   
      loop += 1 
      count_frame = 0
    boolean = True

  ### Turning Rules ###
  else:

    if(ai.selfAlive() == 1):
      
      if frontWall <= frontAlertValue and (left45Wall < right45Wall) and ai.selfSpeed() != 0: 
        #print("turning right")
        ai.turnRight(1)
      elif frontWall <= frontAlertValue and (left45Wall > right45Wall) and ai.selfSpeed() != 0:
        ai.turnLeft(1)
      elif left90Wall <= frontAlertValue and ai.selfSpeed() != 0:
        #print("turning right")
        ai.turnRight(1) 
      elif right90Wall <= frontAlertValue and ai.selfSpeed() != 0:
        #print("turning left")
        ai.turnLeft(1)
      ### Thrust commands ####
      elif ai.selfSpeed() <= speedAlertValue and (frontWall >= frontAlertValue) and (left45Wall >= frontAlertValue) and (right45Wall >= frontAlertValue) and (right90Wall >= frontAlertValue) and (left90Wall >= frontAlertValue) and (left135Wall >= backAlertValue) and (right135Wall >= backAlertValue) and (backWall >= backAlertValue):
        #print("go forward")
        ai.thrust(1)
      elif trackWall < 75 and ai.selfSpeed() >= speedAlertValue:
        ai.thrust(1)
      elif trackWall < 50 and ai.selfSpeed() <= speedAlertValue:
        ai.thrust(1)
      elif backWall <= 75:
        ai.thrust(1)  
      elif left135Wall <= 75:
        ai.thrust(1)
      elif right135Wall <= 75:
        ai.thrust(1)
      ##### Shooting Ennemy Commands #####
      elif enemyDist <= 500 and heading > (head):
        ai.turnRight(1)
        ai.fireShot()
      elif enemyDist <= 500 and heading < (head):
        ai.turnLeft(1)
        ai.fireShot()
      elif ai.selfSpeed() == 0:
        ai.thrust(1)
      else:
        #print("chilling")
        ai.thrust(0)

      count_frame += 1
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


  