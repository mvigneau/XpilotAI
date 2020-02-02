#Evan Gray - January 2018
import libpyAI as ai
def AI_loop():
  #Release keys
  ai.thrust(0)
  ai.turnLeft(0)
  ai.turnRight(0)
  #Set variables
  heading = int(ai.selfHeadingDeg())
  tracking = int(ai.selfTrackingDeg())
  frontWall = ai.wallFeeler(500,heading)
  leftWall = ai.wallFeeler(500,heading+90)
  rightWall = ai.wallFeeler(500,heading-90)
  trackWall = ai.wallFeeler(500,tracking)

  #Thrust rules
  print("i am heading")
  print(heading)
  print(frontWall)
  print(leftWall)
  print(rightWall)
  print("front left right")

  if ai.selfSpeed() <= 5 and frontWall >= 20:
    ai.thrust(1)
  elif trackWall < 20:
    ai.thrust(1)
  #Turn rules
#  if leftWall < rightWall:
#    ai.turnRight(1)
#  else:
#    ai.turnLeft(1)
#------------------------
  degList=[]
  deg=0
  for i in range(9):
      degree = heading+deg
      degList.append(ai.wallFeeler(500,degree))
      deg = deg + 45

  highestDist = 0
  print(degList)
  for element in degList:
      if element >= highestDist:
        highestDist=element
        print("highestDist")
        print(highestDist)
        print("index of highestdist")
        print(degList.index(highestDist))

  ai.turn(heading+((degList.index(highestDist))*45))
  print("the way to turn")
  print(heading+((degList.index(highestDist))*45))
#-------------------------------


  #Just keep shooting
  ai.fireShot()
ai.start(AI_loop,["-name","Dumbo","-join","cc8418"])