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

  if ai.selfSpeed() <= 1 and frontWall >= 20:
    ai.thrust(1)
  elif trackWall < 40:
    ai.thrust(1)
  #Turn rules
  if leftWall < rightWall:
    ai.turnRight(1)
  else:
    ai.turnLeft(1)

  #Just keep shooting
  ai.fireShot()
ai.start(AI_loop,["-name","Dumbo","-join","cc8418"])

