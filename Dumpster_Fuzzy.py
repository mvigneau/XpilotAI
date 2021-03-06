## Mathieu Vigneault, _______ ## 
## 02-14-2020 ##
## Some functions that generates fuzzy inputs and outputs ##

import math

## The function finds the closing rate and the distance for wall in a specified direction ##
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

## Give a degree of membership for slow, medium, fast closing rate ##
def Fuzzy_Speed(Closing_rate, closingRate_SlowTopAlertValue, closingRate_SlowBottomAlertValue, closingRate_MediumBottomLeftAlertValue, closingRate_MediumTopLeftAlertValue, closingRate_MediumTopRightAlertValue, closingRate_MediumBottomRightAlertValue, closingRate_FastBottomAlertValue, closingRate_FastTopAlertValue):
	
	## Step 1 -- Closing Rate; slow, medium or fast ##
	Membership_Slow = 0 
	Membership_Medium = 0
	Membership_Fast = 0
	
	if(Closing_rate <= closingRate_SlowTopAlertValue):
		Membership_Slow = 1
	if(Closing_rate > closingRate_SlowTopAlertValue and Closing_rate < closingRate_SlowBottomAlertValue):
		Membership_Slow  = FindSlope(closingRate_SlowTopAlertValue,1,closingRate_SlowBottomAlertValue,0)
	if(Closing_rate > closingRate_MediumBottomLeftAlertValue and Closing_rate < closingRate_MediumTopLeftAlertValue):
		Membership_Medium = FindSlope(closingRate_MediumBottomLeftAlertValue,1,closingRate_MediumTopLeftAlertValue,0)
	if(Closing_rate >= closingRate_MediumTopLeftAlertValue and Closing_rate <= closingRate_MediumTopRightAlertValue):
		Membership_Medium = 1
	if(Closing_rate > closingRate_MediumTopRightAlertValue and Closing_rate < closingRate_MediumBottomRightAlertValue):
		Membership_Medium = FindSlope(closingRate_MediumTopRightAlertValue,1,closingRate_MediumBottomRightAlertValue,0)
	if(Closing_rate > closingRate_FastBottomAlertValue and Closing_rate < closingRate_FastTopAlertValue):
		Membership_Fast = FindSlope(closingRate_FastBottomAlertValue,1,closingRate_FastTopAlertValue,0)
	if (Closing_rate >= closingRate_FastTopAlertValue): 
			Membership_Fast = 1
	
	return (Membership_Slow, Membership_Medium, Membership_Fast)

## Give a degree of membership for ditance; close or far ##
def Fuzzy_Distance(Distance, Distance_CloseTopAlertValue, Distance_CloseBottomAlertValue, Distance_FarBottomAlertValue, Distance_FarTopAlertValue):	
	
	## Step 2 -- Distance; close or far ##
	Distance_Close = 0
	Distance_Far = 0

	if(Distance <= Distance_CloseTopAlertValue):
		Distance_Close = 1
	if(Distance > Distance_CloseTopAlertValue and Distance < Distance_CloseBottomAlertValue):
		Distance_Close = FindSlope(Distance_CloseTopAlertValue,1,Distance_CloseBottomAlertValue,0)
	if(Distance > Distance_FarBottomAlertValue and Distance < Distance_FarTopAlertValue):
		Distance_Far = FindSlope(Distance_FarBottomAlertValue,1,Distance_FarTopAlertValue,0)
	if(Distance >= Distance_FarTopAlertValue):
		Distance_Far = 1
	
	return(Distance_Close, Distance_Far)

## Fuzzy rules to determine output in terms of risks and defuzification ##
def Fuzzy_Risk(Membership_Slow, Membership_Medium, Membership_Fast, Distance_Close, Distance_Far):
	
	## Linguistic variable for output == risk ##
	## risk can be either low, medium, high based off the inputs; distance, closing_rate ##
	risk_low = 0
	risk_medium = 0
	risk_high = 0
	
	if(Distance_Close > 0):
		risk_high = Distance_Close
	if(Membership_Slow > 0 and Distance_Close > 0):
		risk_medium = min(Membership_Slow, Distance_Close)
	if(Membership_Slow > 0 and Distance_Far > 0):
		risk_low = min(Membership_Slow, Distance_Far)
	if(Membership_Fast > 0 and Distance_Close > 0):
		risk_high = min(Membership_Fast, Distance_Close)
	if(Membership_Fast > 0 and Distance_Far > 0):
		risk_medium = min(Membership_Fast, Distance_Far)
	if(Membership_Medium > 0 and Distance_Far > 0):
		risk_medium = min(Membership_Medium, Distance_Far)
	if(Membership_Medium > 0 and Distance_Close > 0):
		risk_high = min(Membership_Medium, Distance_Close)
	if(Membership_Slow > 0 or Distance_Far > 0):
		risk_low = max(Membership_Slow, Distance_Far)
	
	total_risk = (risk_low * 25 + risk_medium * 50 + risk_high * 75) / (risk_low + risk_medium + risk_high)
	
	return total_risk

def FindSlope(x1, y1, x2, y2):

	x_change = abs(x2-x1)
	y_change = abs(y2-y1)

	slope = round((y_change/x_change),3)
	return slope

	