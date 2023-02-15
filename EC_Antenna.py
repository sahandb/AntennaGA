# imports
import numpy as np
import matplotlib.pyplot as plt
import random
from copy import deepcopy

fit_sum_list = list()
mean_fit_sum_list = list()


# selection
def tournament(fitness_population, k):
    best = 0
    for i in range(k):
        ind = random.sample(fitness_population, 1)
        if best == 0 or ind > best:
            best = ind
    return best


# Tournament Selection
def selection(populationi, populationx, populationy, fit):
    probabilities = list()
    for i in range(len(populationi)):
        tournament(fit, 3)
        probabilities = (populationi[i], populationx[i], populationy[i])
        break
    return probabilities


# Roulette Selection
# def selection(roulette,n):
#     probabilities = list()
#     for j in range(n):
#         rand = random.random()
#         for i in range(len(population)):
#             if rand <= roulette[i]:
#                 probabilities.append(population[i])
#                 break
#     return probabilities

# fitness function
def fitness(popi, popx, popy):
    population_fitness = list()
    cost = 0
    antennaCoverage = 0
    for i in range(m):
        for j in range(n):
            for g in range(10):
                if dist(popx[g], i, popy[g], j) <= popi[g]:
                    cost = + popi[g]
                    antennaCoverage = + 1
                    break

    fit = antennaCoverage - cost
    population_fitness.append(fit)
    return population_fitness


# Euclidean distance
def dist(x2, x1, y2, y1):
    return np.sqrt(np.sum((x2 - x1) ** 2, (y2 - y1) ** 2))


# crossover one-point with random split
def crossover(parent1, parent2):
    split = random.randint(0, 10)
    parent1 = deepcopy(parent1)
    parent2 = deepcopy(parent2)
    child1 = np.concatenate((parent1[0:split], parent2[split:]))
    child2 = np.concatenate((parent2[0:split], parent1[split:]))
    return child1, child2


# crossover 2-point with random split
def twoPointCrossover(parent1, parent2):
    # Randomly select the two crossover points
    crossover_points = [random.randint(0, 10)]
    second_point = random.randint(0, 10)
    while second_point == crossover_points[0]:
        second_point = random.randint(0, 10)
    crossover_points.append(second_point)
    parent1 = deepcopy(parent1)
    parent2 = deepcopy(parent2)
    child1 = np.concatenate((parent1[0:crossover_points[0]], parent2[crossover_points[0]:]))
    child2 = np.concatenate((parent2[0:crossover_points[1]], parent1[crossover_points[1]:]))
    return child1, child2


# mutation less than 0.005 random
def mutation(a):
    for i in range(100):
        rand = random.random()
        if rand <= 0.005:
            a[i][0] = random.randint(0, 10)
    return a


# main algorithm
def GA(populationi, populationx, populationy, iter):
    parent_geni = populationi
    parent_genx = populationx
    parent_geny = populationy
    k = len(populationi)

    for i in range(iter):
        for f in range(k):
            fit = fitness(parent_geni[f], parent_genx[f], parent_geny[f])
            eliteFit = max(fit)
            badFit = min(fit)

        fit_sum = float(sum(fit))

        mean_fit_sum = float(fit_sum / 100)
        print("{}.{} {}".format(i + 1, "fitness :", fit_sum))
        # list for plot
        fit_sum_list.append(fit_sum)
        #
        mean_fit_sum_list.append(mean_fit_sum)

        # # Roulette Selection
        # portion_fitness = [f / fit_sum for f in fit]
        # roulette = [sum(portion_fitness[:i + 1]) for i in range(len(portion_fitness))]

        offspring = list()

        # crossover in algorithm
        for j in range(k):
            parent1 = selection(parent_geni[j], parent_genx[j], parent_geny[j], fit)
            parent2 = selection(parent_geni[j], parent_genx[j], parent_geny[j], fit)

            child1, child2 = crossover(parent1, parent2)
            offspring.append(child1)
            offspring.append(child2)
        # mutation in algorithm
        for j in range(k):
            parent = selection(parent_geni[j], parent_genx[j], parent_geny[j], fit)
            child = mutation(parent)
            offspring.append(child)


# population number populationi = np.zeros((10, 100)) populationx = np.zeros((10, 100)) populationy = np.zeros((10,
# 100)) i number of antenna 0 mean no antenna and 1 to 10 radios and even cost , x and y 0 to m and 0 to n for
# location of antenna
populationi = np.random.randint(0, 10, [100, 10])
populationx = np.random.randint(0, 25, [100, 10])
populationy = np.random.randint(0, 25, [100, 10])

m = 25
n = 25
GA(populationi, populationx, populationy, 1000)
