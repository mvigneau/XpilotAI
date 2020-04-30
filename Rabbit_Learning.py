### Program 1 -- Mathieu Vigneault,  
import libpyAI as ai
from Rabbit_GA import * 

### Setting Up GA ###
population_size = 1
crossover_prob = 0.7
mutation_prob = 0.01
chromosome_size = 13
fitness_target = 20
population = init_population(population_size, chromosome_size)
count_frame = 0


def AI_loop():

  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)
  print(ai.selfAlive())
  #for chrom in range(len(population)):
  chrom = 0
  print("pop", population)
  current_chromosome = population[chrom]
  print(current_chromosome)
  frontAlert = current_chromosome[0:5]
  print("frontAlert", frontAlert)
  frontAlertValue = transform(frontAlert, 25)
  print("frontAlertValue", frontAlertValue)
  backAlert = current_chromosome[5:9]
  backAlertValue = transform(backAlert, 25)
  print("backAlertValue", backAlertValue)
  speedAlert = current_chromosome[9:13]
  speedAlertValue = transform(speedAlert, 1)
  print("speedAlertValue", speedAlertValue)

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
  print(enemy)
  head = ai.lockHeadingDeg()
  print(head)
  enemyDist = ai.selfLockDist()
  print(enemyDist)
  
  if ai.selfAlive() == 0: 
     print(count_frame)
  ### Turning Rules ###
  else:
    global count_frame 
    count_frame += 1
    if ai.selfSpeed() == 0:
      ai.thrust(1)
    elif frontWall <= frontAlertValue and (left45Wall < right45Wall): 
      print("turning right")
      ai.turnRight(1)
    elif frontWall <= frontAlertValue and (left45Wall > right45Wall):
      ai.turnLeft(1)
    elif left90Wall <= frontAlertValue:
      print("turning right")
      ai.turnRight(1) 
    elif right90Wall <= frontAlertValue:
      print("turning left")
      ai.turnLeft(1)
    ### Thrust commands ####
    elif ai.selfSpeed() <= speedAlertValue and (frontWall >= frontAlertValue) and (left45Wall >= frontAlertValue) and (right45Wall >= frontAlertValue) and (right90Wall >= frontAlertValue) and (left90Wall >= frontAlertValue) and (left135Wall >= backAlertValue) and (right135Wall >= backAlertValue) and (backWall >= backAlertValue):
      print("go forward")
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
    else:
      print("chilling")
      ai.thrust(0)

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

ai.start(AI_loop,["-name","Rabbit","-join","localhost"])


  