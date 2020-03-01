import random
import math

#Create random weights between -0.5 and 0.5
def create_weights(list1):
	i = 0
	weights = []
	if isinstance(list1, list):
		for i in range(len(list1)):
			weight = random.uniform(-0.5,0.5)
			weights.append(weight)
	else:
		fo#Create random weights between -0.5 and 0.5
def create_weights(list1):
	i = 0
	weights = []
	if isinstance(list1, list):
		for i in range(len(list1)):
			weight = random.uniform(-0.5,0.5)
			weights.append(weight)
	else:
		for i in range(list1):
			weight = random.uniform(-0.5,0.5)
			weights.append(weight)
	return weights

#Sigmoid function for squashing
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

#Multiply the weights against the inputs
def multi(weights, input_list):
	i = 0
	layer = []
	for i in range(len(input_list)):
		new = input_list[i] * weights[i]
		layer.append(new)
	return layer

#Two functions to weight train
#Function from input nodes into hidden layers
def output_layer_grad(weights, output, hidden_output, desired_output, learning_rate):
	#Calculate the error
	error = desired_output - output
	#Calculating the error gradient
	gradient = output * (1-output) * error
	#Correcting the weights
	for i in range(len(weights)):
		change = learning_rate * hidden_output[i] * gradient
		weights[i] = weights[i] + change
	return weights

#Fixing weights from hidden layers to output
def hidden_layer_grad(weights, weights2, input_nodes, hidden_layer, desired_output, output, learning_rate):
	#Calculating the error
	error = desired_output - output
	#Calculating the gradient from nuerons in the hidden layer
	gradient = (output * (1-output)) * error
	gradient2list = []
	#Calculating the weight corrections
	for i in range(len(hidden_layer)-1):
		gradient2 = (hidden_layer[i] * (1-hidden_layer[i])) * (gradient * weights2[i])
		gradient2list.append(gradient2)
	for k in range(len(weights)):
		#Updating the weights at the hidden neurons
		for l in range(len(weights[0])):
			change = learning_rate * input_nodes[l] * gradient2list[k]
			weights[k][l] = weights[k][l] + change
	return weights


def NN():
	#Setting learning rate, epochs, and hidden nodes
	learning_rate = 0.3
	epochs = 10000
	hidden_nodes = 3

	#Input list
	in_out_list = 	[[[0,0,0,0,0],0],
			[[0,0,0,0,1],0.2],
			[[0,0,0,1,0],0.2],
			[[0,0,1,0,0],0.2],
			[[0,1,0,0,0],0.2],
			[[1,0,0,0,0],0.2],
			[[0,0,0,1,1],0.4],
			[[0,0,1,0,1],0.4],
			[[0,1,0,0,1],0.4],
			[[1,0,0,0,1],0.4],
			[[0,0,1,1,0],0.4],
			[[0,1,0,1,0],0.4],
			[[1,0,0,1,0],0.4],
			[[0,1,1,0,0],0.4],
			[[1,0,1,0,0],0.4],
			[[1,1,0,0,0],0.4],
			[[0,0,1,1,1],0.6],
			[[0,1,0,1,1],0.6],
			[[1,0,0,1,1],0.6],
			[[0,1,1,0,1],0.6],
			[[1,0,1,0,1],0.6],
			[[1,1,0,0,1],0.6],
			[[0,1,1,1,0],0.6],
			[[1,0,1,1,0],0.6],
			[[1,1,0,1,0],0.6],
			[[1,1,1,0,0],0.6],
			[[0,1,1,1,1],0.8],
			[[1,0,1,1,1],0.8],
			[[1,1,0,1,1],0.8],
			[[1,1,1,0,1],0.8], 
			[[1,1,1,1,0],0.8],
			[[1,1,1,1,1],1]]

	#Creating random weights
	weights1 = []
	for i in range(len(in_out_list)):
		in_out_list[i][0].append(-1)
	for k in range(hidden_nodes):
		weights = create_weights(in_out_list[0][0])
		weights1.append(weights)
	weights2 = create_weights(hidden_nodes+1)

	
	activationlist = []
	for i in range(epochs):
		for j in range(len(in_out_list)):
			#Calculating the ouput from the hidden layer
			layer1_output = []
			for k in range(hidden_nodes):
				new_output = multi(weights1[k], in_out_list[j][0])
				adder = 0
				for m in range(len(new_output)):
					adder = new_output[m] + adder
				activation = sigmoid(adder)
				layer1_output.append(activation)
			layer1_output.append(-1)

			#Calcuating output from nerual network
			output_layer = multi(weights2, layer1_output)
			adder = 0
			for k in range(len(output_layer)):
				adder = output_layer[k] + adder
			output = sigmoid(adder)
			activationlist.append(output)

			#Activating weights 
			update_weights2 = output_layer_grad(weights2, output, layer1_output, in_out_list[j][1], learning_rate)
			weights1 = hidden_layer_grad(weights1, weights2, in_out_list[j][0], layer1_output, in_out_list[j][1], output, learning_rate)
			weights2 = update_weights2

	#Printing the final outputs
	#for j in range(len(in_out_list)):
	#	print(in_out_list[j][0], activationlist[-j+1])
	#print(activationlist[-32:])
	print(weights1)
	print(weights2)

NN()