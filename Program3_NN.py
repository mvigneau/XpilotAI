import random
import math

def Data(enemyDist, ClosestSpeed, ClosestDir, head, heading, tracking):
	
	input1 = 0
	input2 = 0
	input3 = 0 
	input4 = 0
	input5 = 0
	
	if(head <= heading):
		input1 = 1
	
	if(ClosestSpeed >= 10):
		input2 = 1
	
	if(ClosestDir != None):
		if(ClosestDir <= 90 or ClosestDir >= 270):
			input3 = 1
	
	if(enemyDist >= 500):
		input4 = 1
	
	if(tracking >= 90 and tracking <= 270 and input3 == 1):
		input5 = 1
		
	return(input1, input2, input3, input4, input5)
	

#Sigmoid function for squashing
def sigmoid(x):
	return 1 / (1 + math.exp(-x))


def Out(input1, input2, input3, input4, input5):
	
	### Hidden Layer ###
	Hidden1 = (input1 *  1.74855104293633 + input2 * 1.7560572359422804 + input3 * 1.7407629699975962 + input4 * 1.743846619646666 + input5 * 1.7217269770025017) - 0.08374950665748468 
	Hidden1_1 = sigmoid(Hidden1) 
	
	Hidden2 = (input1 *  -1.0024533201560595 + input2 * -1.003792766826858 + input3 * -1.001690958097889 + input4 * -1.00354322793587 + input5 * -1.0033624801466616) - (-4.843878340611762)
	Hidden2_1 = sigmoid(Hidden2) 
	Hidden3 = (input1 *  -0.7918225811311883 + input2 * -0.7864290587369103 + input3 * -0.7964018801120206 + input4 * -0.7924517172466758 + input5 * -0.802488981898789) - (-0.13199966998848878)
	Hidden3_1 = sigmoid(Hidden3) 
	
	### Output ###
	output = (Hidden1_1 * 3.9272363560103187 + Hidden2_1 * -5.636922806626904 + Hidden3_1 * -2.2103317988269198) - (-1.5536092228594287) 
	output_1 = sigmoid(output) 
	
	return output_1