import random

N = 5
POP_SIZE = 6
MAX_GENERATIONS = 100

# Generate a chromosome
def generate_chromosome():
    return random.sample(range(N), N)

# Fitness function: number of non-attacking pairs
def fitness(chromosome):
    non_attacking = 0
    total_pairs = N * (N - 1) // 2

    attacking = 0

    for i in range(N):
        for j in range(i + 1, N):

            # same row
            if chromosome[i] == chromosome[j]:
                attacking += 1

            # same diagonal
            if abs(chromosome[i] - chromosome[j]) == abs(i - j):
                attacking += 1

    non_attacking = total_pairs - attacking
    return non_attacking


# Tournament Selection
def tournament_selection(population):
    a = random.choice(population)
    b = random.choice(population)

    if fitness(a) > fitness(b):
        winner = a
    else:
        winner = b

    print("Tournament between", a, "and", b, "Winner:", winner)
    return winner


# Crossover
def crossover(parent1, parent2):
    point = random.randint(1, N-2)

    child = parent1[:point] + parent2[point:]
    return child


# Swap Mutation
def mutation(chromosome):
    i, j = random.sample(range(N), 2)

    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

    print("Mutation (swap positions", i, "and", j, "):", chromosome)
    return chromosome


# Initial Population
population = [generate_chromosome() for _ in range(POP_SIZE)]

print("Initial Population:", population)

for generation in range(MAX_GENERATIONS):

    print("\nGeneration", generation)

    new_population = []

    for _ in range(POP_SIZE):

        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        child = crossover(parent1, parent2)

        if random.random() < 0.3:
            child = mutation(child)

        new_population.append(child)

        print("Child:", child, "Fitness:", fitness(child))

        if fitness(child) == 10:
            print("\nSolution Found:", child)
            exit()

    population = new_population

print("\nFinal Population:", population)