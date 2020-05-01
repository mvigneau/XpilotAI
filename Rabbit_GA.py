### Mathieu Vigneault
### 03-23-2020
### Here is my genetic algorithm it eventually finds the answer
### but it is a bit too long at my taste, might be due to selection
### process not strict enough ... will fix it soon

from random import *
import matplotlib.pyplot as plt

population_size = 8
crossover_prob = 0.7
mutation_prob = 0.01
chromosome_size = 13
fitness_target = 20


## Initialize population & Fitness Score##
def init_population(population_size, chromosome_size):
	population_list = []
	for i in range(population_size):
		chromosome = []
		for j in range(chromosome_size):

			number = int(round(random(),0))
			chromosome.append(number)

		population_list.append(chromosome) 
	
	return population_list


def fitness(chromosome, frames):

	return frames
	# for j in range(len(population_list[i])):
	# 	if population_list[i][j] == 1:
	# 		fitness_score += 1

	# fitness_list.append(fitness_score)

	# return fitness_list

def check_fitness(fitness_list):

	maximum = 0
	for i in range(len(fitness_list)):
		if fitness_list[i] == fitness_target:
			return fitness_target
		else: 
			if fitness_list[i] > maximum:
				maximum = fitness_list[i]
	return maximum

## Selection Process ## 
def select(population_list, fitness_list, new_population):
	#print(new_population)
	
	total = 0 
	for i in range(len(fitness_list)):
		total += fitness_list[i]

	probability_list = []
	for j in range(len(fitness_list)):
		prob = float(fitness_list[j]) / total
		probability_list.append(prob)

	## Select a pair of chromosomes ##
	selection1 = choices(population_list, probability_list)
	selection2 = choices(population_list, probability_list)
	
	new_population.append(selection1[0])
	new_population.append(selection2[0])
	return new_population

def crossover(new_population):
	#print(new_population)
	
	random_number = randint(1, 100)
	if random_number <= (crossover_prob * 100):
		chrom = randrange(0,2)
		spot = randrange(0,20)
		#print(chrom, spot)

		if chrom == 0:
			chromosome1_part1 = new_population[0][:spot]
			chromosome1_part2 = new_population[1][spot:]
			chromosome2_part1 = new_population[1][:spot]
			chromosome2_part2 = new_population[0][spot:]
		else:
			chromosome1_part1 = new_population[1][:spot]
			chromosome1_part2 = new_population[0][spot:]
			chromosome2_part1 = new_population[0][:spot]
			chromosome2_part2 = new_population[1][spot:]

		chromosome1 = chromosome1_part1 + chromosome1_part2
		chromosome2 = chromosome2_part1 + chromosome2_part2
		
		new_population.pop()
		new_population.pop()

		new_population.append(chromosome1)
		new_population.append(chromosome2)

	return new_population

def mutate(new_population):
	#print(new_population)
	
	for i in range(len(new_population)):
		for j in range(chromosome_size):
			random_number = randint(1, 100)
			if random_number <= (mutation_prob * 100):
				#print(i,j)
				#print(new_population[i][0][j])
				if new_population[i][j] == 0:
					new_population[i][j] = 1
				else:
					new_population[i][j] = 0
				#print(new_population[i][0][j])
	#print(new_population)
	return new_population 


def transform(gene, jump):
	value = 0
	gene.reverse()
	for i in range(len(gene)):
		if (gene[i] == 1):
			value += (jump * (2**(i)))
	return value




# def main():

# 	### Initiate a population ###
# 	population_list = init_population()
# 	found = False
# 	counter = 0 
# 	data = []
# 	while found == False:
# 		### Get fitness of population ###
# 		fitness_list = fitness(population_list)
# 		### Check if fitness target is reached ###
# 		result = check_fitness(fitness_list)
		
# 		if counter % 10 == 0:
# 			point = (counter, result)
# 			data.append(point)
# 			#print(data)

# 		if result == fitness_target:
# 			found = True

# 		### Creating a new population ##
# 		new_population = []

# 		while(len(new_population) != population_size):

# 			### Select a pair of chromosomes ###
# 			new_population = select(population_list, fitness_list, new_population)
# 			### Apply crossover on it ###
# 			new_population = crossover(new_population)

# 		### Apply mutation to new population ###
# 		new_population = mutate(new_population)
# 		population_list = new_population
# 		counter += 1
# 	#print(new_population)
# 	print(result)
# 	zip(*data)
# 	plt.scatter(*zip(*data))
# 	plt.axis([0, len(data), 0, 21])
# 	plt.show()
	

# main()
