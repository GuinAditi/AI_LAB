import random

N = 5
POP_SIZE = 4

# Generate chromosome
def generate_chromosome():
    return random.sample(range(N), N)

# Fitness function
def fitness(chromosome):
    total_pairs = N*(N-1)//2
    attacking = 0

    for i in range(N):
        for j in range(i+1, N):

            if chromosome[i] == chromosome[j]:
                attacking += 1

            if abs(chromosome[i]-chromosome[j]) == abs(i-j):
                attacking += 1

    return total_pairs - attacking


# Print board
def print_board(chromosome):

    board = [["." for _ in range(N)] for _ in range(N)]

    for col in range(N):
        row = chromosome[col]
        board[row][col] = "Q"

    print("\nBoard Representation")

    for r in board:
        print("|", " | ".join(r), "|")


# Initial Population
population = [generate_chromosome() for _ in range(POP_SIZE)]

print("Initial Population (Chromosomes)\n")

for i, chrom in enumerate(population):

    print("Solution", i+1)
    print("Chromosome:", chrom)
    print("Fitness:", fitness(chrom))

    print_board(chrom)

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