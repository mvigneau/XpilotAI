import math

def Closing_Rate(Degree, tracking, Speed, Distance):
	
	angle = Degree - tracking
	
	if(angle >= 0 and angle <= 90): 
		#angle = Degree - tracking
		angle_opposite = 180 - 90 - angle
		radian = math.radians(angle_opposite)
		closing_rate = round(Speed * math.sin(radian),4)
		distance = Distance 
	elif(angle >= 90 and angle <= 180):
		angle_opposite = 180 - 90 - (180-angle)
		radian = math.radians(angle_opposite)
		closing_rate = round(Speed * math.sin(radian) * (-1),4)
		distance = Distance
	elif(angle >= 180 and angle <= 270):
		angle_opposite = 180 - 90 - (angle-180)
		radian = math.radians(angle_opposite)
		closing_rate = round(Speed * math.sin(radian) * (-1),4)
		distance = Distance
	else:
		angle_opposite = 180 - 90 - (90-(angle-270))
		radian = math.radians(angle_opposite)
		closing_rate = round(Speed * math.sin(radian),4)
		distance = Distance
		
	return closing_rate, distance

def Fuzzy(Closing_rate, Distance):
	
	## Step 1 -- Closing Rate; slow, medium or fast ##
	Membership_Slow = 0 
	Membership_Medium = 0
	Membership_Fast = 0
	
	if(Closing_rate <= 3):
		Membership_Slow = 1
	if(Closing_rate > 3 and Closing_rate < 5):
		Membership_Slow = round(-0.5 * Closing_rate + 2.5,3)
	if(Closing_rate > 3 and Closing_rate < 5):
		Membership_Medium = round(0.5 * Closing_rate - 1.5,3)
	if(Closing_rate >= 5 and Closing_rate <= 6):
		Membership_Medium = 1
	if(Closing_rate > 6 and Closing_rate < 8):
		Membership_Medium = round(-0.5 * Closing_rate + 4, 3)
	if(Closing_rate > 6 and Closing_rate < 8):
		Membership_Fast = round(0.5 * Closing_rate - 3,3)
	if (Closing_rate >= 8): 
			Membership_Fast = 1
	
	print(Membership_Slow, Membership_Medium, Membership_Fast)
	
	return 0
	