
# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
#                           Q1
# ////////////////////////////////////////////////////////////////////////
import random
import time

# ////////////////////////////////////////////////////////////////////
# //   for getting the time execute
start_time = time.time()


def random_chromosome(size):  # making random chromosomes
    #     return [ random.randint(1, nq) for _ in range(nq) ]
    # /////////////////////////////////////////////////////////////////
    # //   we should change the population if we want to use PMX algorithm otherewise you we get
    # //   Error (error about the length of chromosome)
    return random.sample(range(1, nq + 1), nq)


def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen) - 1 for queen in chromosome]) / 2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(maxFitness - (horizontal_collisions + diagonal_collisions))  # 28-(2+3)=23


def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness


def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
# ///////////////////////////////////////////////////////////////////////
# //        default function
def reproduce(x, y):  # doing cross_over between two chromosomes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]




# //////////////////////////////////////////////////////////////////////////
# //        Q1-1  PMX
def reproduce(x, y):  # doing cross_over between two chromosomes
    n = len(x)
    #     print("x",x)
    #     print("y",y)

    # /////////////////////////////////////////////////////////////////////////////////////////
    # //      create two sample code between (0,n-1) , random number (sample) does not repetitive
    c = random.sample(range(0, n - 1), 2)
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
    #     c = random.randint(0, n - 1)
    #     return x[0:c] + y[c:n]
    return t
# //////////////////////////////////////////////////////////////////////////
# ///           Q1-2
def mutate(x):  # randomly changing the value of a random index of a chromosome
    n = len(x)
    c1 = random.randint(0, n - 1)
    c2 = random.randint(0, n - 1)
    m = x[c1]
    x[c1] = x[c2]
    x[c2] = m
    return x

# //////////////////////////////////////////////////////////////////////////
# //        Q2
def reproduce(x, y ):  # select chromosome and gen randomly
    n = len(x)
    #     print("x",x)
    #     print("y",y)
    t = []
    index = 0
    while index <n:
        select = random.randint(0, 1)
        match = random.randint(0, 1)
        i  = random.randint(0,n-1)
        if x[i] not in t and  select == match:
            t.append(x[i])
            index +=1
        else :
            if y[i] not in t:
                t.append(y[i])
                index +=1

    return t
def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities)  # best chromosome 1
        y = random_pick(population, probabilities)  # best chromosome 2
        child = reproduce(x, y )  # creating two new chromosomes from the best 2 chromosomes
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population


def print_chromosome(chrom):
    print("Chromosome = {},  Fitness = {}"
          .format(str(chrom), fitness(chrom)))


if __name__ == "__main__":
    #     nq = int(input("Enter Number of Queens: ")) #say N = 8
    nq = 8
    maxFitness = (nq * (nq - 1)) / 2  # 8*7/2 = 28
    population = [random_chromosome(nq) for _ in range(100)]

    generation = 1

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("")
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}!".format(generation - 1))
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("");
            print("One of the solutions: ")
            chrom_out = chrom
            print_chromosome(chrom)

    board = []

    for x in range(nq):
        board.append(["x"] * nq)

    for i in range(nq):
        board[nq - chrom_out[i]][i] = "Q"


    def print_board(board):
        for row in board:
            print(" ".join(row))


    print()
    print_board(board)
    print()
    print("--- %s seconds ---" % (time.time() - start_time))



