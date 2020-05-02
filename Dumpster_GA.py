### Mathieu Vigneault
### 05-1-2020
### Here is some function for a genetic algorithm
### but it is a bit too long at my taste, might be due to selection
### process not strict enough ... will fix it soon

from random import *
import matplotlib.pyplot as plt


## Initialize population given a population size and a chrosomone size ##
def init_population(population_size, chromosome_size):
	population_list = []
	for i in range(population_size):
		chromosome = []
		for j in range(chromosome_size):

			number = int(round(random(),0))
			chromosome.append(number)

		population_list.append(chromosome) 
	
	return population_list

## Calculate the Fitness on an agent based on survival time, death reault and kill result ##
def fitness(chromosome, frames, score_previous, score_current):

	value = 0
	if(abs(score_previous - score_current) == 3.4):
		value -= 40
	elif((score_current - score_previous) > 0):
		value += 120
	else:
		value -= 80

	value += frames
	return value

## Selection Process based on the fitness of the individuals ##
## Higher fitness has a higher chance of reproducing to the next generation ##  
def select(population, fitness_list):
	
	## Calculate Sum of Total Fitness of Entire Population ##
	total = 0 
	for i in range(len(fitness_list)):
		total += fitness_list[i]

	## Calculate Probability to Select Each Individual ##
	probability_list = []
	for j in range(len(fitness_list)):
		prob = float(fitness_list[j]) / total
		probability_list.append(prob)

	## Repeat these step until you fill up entire new population ##
	new_population = []
	for popsize in range(len(population)):
		## Select A Chromosome ##
		selection = choices(population, probability_list)
	
		## Add Selected Chromosome to New Population ##
		new_population.append(selection[0])

	return new_population

def crossover(new_population, chromosome_size, population_size, crossover_prob):
	#print(new_population)
	storage = []
	for half in range((len(new_population)//2)):
		random_number = randint(1, 100)
		if random_number <= (crossover_prob * 100):
			parent1 = randrange(0, len(new_population))
			parent2 = randrange(0, len(new_population))
			while(parent1 == parent2):
				parent2 = randrange(0, len(new_population))
			chrom = randrange(0,2)
			spot = randrange(0,chromosome_size)
			#print(chrom, spot, parent1, parent2)

			if chrom == 0:
				chromosome1_part1 = new_population[parent1][:spot]
				chromosome1_part2 = new_population[parent2][spot:]
				chromosome2_part1 = new_population[parent2][:spot]
				chromosome2_part2 = new_population[parent1][spot:]
			else:
				chromosome1_part1 = new_population[parent2][:spot]
				chromosome1_part2 = new_population[parent1][spot:]
				chromosome2_part1 = new_population[parent1][:spot]
				chromosome2_part2 = new_population[parent2][spot:]

			chromosome1 = chromosome1_part1 + chromosome1_part2
			chromosome2 = chromosome2_part1 + chromosome2_part2
			
			if(parent1 < parent2):
				new_population.pop(parent1)
				new_population.pop(parent2-1)
			else:
				new_population.pop(parent2)
				new_population.pop(parent1-1)

			storage.append(chromosome1)
			storage.append(chromosome2)

	for num in range(len(storage)):
		#print(storage[num])
		new_population.append(storage[num])

	return new_population

def mutate(new_population, chromosome_size, mutation_prob):
	
	for i in range(len(new_population)):
		for j in range(chromosome_size):
			random_number = randint(1, 100)
			if random_number <= (mutation_prob * 100):
				if new_population[i][j] == 0:
					new_population[i][j] = 1
				else:
					new_population[i][j] = 0

	return new_population 


def transform(gene, jump):
	value = 0
	gene.reverse()
	for i in range(len(gene)):
		if (gene[i] == 1):
			value += (jump * (2**(i)))
	return value

def transform_fuzzy(gene, jump, start, end):
	#print(gene, jump, start, end)
	value = start
	gene.reverse()
	threshold = 100000
	while(threshold > end):
		current_value = 0
		for i in range(len(gene)):
			if (gene[i] == 1):
				current_value += (jump * (2**(i)))
		threshold = current_value
		print(threshold)

	value += current_value
	
	return value

