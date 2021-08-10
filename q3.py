
# ////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# //                    Q 3
import random
import pandas as pd
import numpy as np


def random_chromosome(size):  # making random chromosomes
    rc = []
    i = 0
    while i < nCity:
        value = random.randint(0, nCity - 1)
        if value not in rc:
            rc.append(value)
            i = i + 1
    return rc


#     return [ random.randint(0, nq-1) for _ in range(nq) ]

def fitness(chromosome):
    length = 0
    for i in range(19):
        xx = cityLocation.iloc[chromosome[i]]["x"] - cityLocation.iloc[chromosome[1 + i]]["x"]
        yy = cityLocation.iloc[chromosome[i]]["y"] - cityLocation.iloc[chromosome[1 + i]]["y"]
        re = (pow(xx, 2) + pow(yy, 2))
        length += re
    return length


# def probability(chromosome, fitness):
#     return fitness(chromosome) / maxFitness


def getPop(popdist, ave):
    for p, d in popdist:
        if d > ave:
            ave += ave
            return getPop(popdist, ave)
        else:
            return p


def random_pick(population, distance):
    popdist = zip(population, distance)
    ave = np.mean(distance)
    population = getPop(popdist, ave)
    return population


def reproduce(x, y):  # doing cross_over between two chromosomes
    n = len(x)
    #     print("len x,y=",x,y)
    #     print("x",x)
    #     print("y",y)

    # /////////////////////////////////////////////////////////////////////////////////////////
    # //      create two sample code between (0,n-1) , random number (sample) does not repetitive
    c = random.sample(range(0, n), 2)
    # ////////////////////////////////////////////////////////////////////////////////////////
    # //      sort sample for better performance , [2,1] sort -> [1,2]
    c.sort()
    #     print("[c1,c2]=",c)
    # ////////////////////////////////////////////////
    # //       adding first part of chromosome (x) to (t)
    t = x[0:c[0]]
    for i in y:
        # ////////////////////////////////////////////////////////////////
        # //    cheking the value in first part of  chromosome (x) and the end part of (x)
        if i not in t and i not in x[c[1]:]:
            # //////////////////////////////////////////////////////////////////////////////
            # //    then add new value to chromose (t) and prevent the repetitive numbers in (t)
            t.append(i)
    t = t + x[c[1]:]

    return t


def mutate(x):  # randomly changing the value of a random index of a chromosome
    n = len(x)
    c1 = random.randint(0, n - 1)
    c2 = random.randint(0, n - 1)
    m = x[c1]
    x[c1] = x[c2]
    x[c2] = m
    return x


def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    distance = [fitness(n) for n in population]
    for i in range(len(population)):
        x = random_pick(population, distance)  # best chromosome 1
        y = random_pick(population, distance)  # best chromosome 2
        child = reproduce(x, y)  # creating two new chromosomes from the best 2 chromosomes
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chromosome(child)
        new_population.append(child)

    return new_population


def print_chromosome(chrom):
    print("Chromosome = {},  Fitness = {}"
          .format(str(chrom), fitness(chrom)))


if __name__ == "__main__":
    cityLocation = pd.read_csv("E:/University/Hoshmohasebati/cityLocation.csv")

    nCity = 20
    population = [random_chromosome(nCity) for _ in range(100)]

    generation = 1
    while generation < 100:
        [fitness(chrom) for chrom in population]
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("")
        print("Minimum Fitness = {}".format(min([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation - 1))
