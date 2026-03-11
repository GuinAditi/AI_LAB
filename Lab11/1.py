import random

N = 5
POP_SIZE = 4
MUTATION_RATE = 0.3
MAX_GENERATIONS = 100


def generate_chromosome():
    return random.sample(range(1, N+1), N)


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


def print_board(chromosome):

    board = [["." for _ in range(N)] for _ in range(N)]

    for col in range(N):
        row = chromosome[col] - 1
        board[row][col] = "Q"

    print("    1  2  3  4  5")

    for i in range(N):
        print(i+1, "|", " ".join(board[i]))


def tournament_selection(population):

    a = random.choice(population)
    b = random.choice(population)

    if fitness(a) > fitness(b):
        return a
    else:
        return b


def crossover(p1, p2):

    point = random.randint(1, N-2)

    child = p1[:point] + p2[point:]

    return child


def mutation(chromosome):

    i, j = random.sample(range(N), 2)

    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

    return chromosome


# ---------------- MAIN PROGRAM ----------------

population = [generate_chromosome() for _ in range(POP_SIZE)]

print("\n========== INITIAL POPULATION ==========\n")

for i, chrom in enumerate(population):

    print("Solution", i+1)
    print("Chromosome:", chrom)
    print("Fitness:", fitness(chrom))
    print_board(chrom)
    print()


generation = 0

while generation < MAX_GENERATIONS:

    print("\n=========== GENERATION", generation+1, "===========\n")

    new_population = []

    for _ in range(POP_SIZE):

        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        child = crossover(parent1, parent2)

        if random.random() < MUTATION_RATE:
            child = mutation(child)

        new_population.append(child)

        print("Child:", child, "Fitness:", fitness(child))

        if fitness(child) == 10:

            print("\n🎉 SOLUTION FOUND 🎉")
            print("Chromosome:", child)

            print_board(child)

            exit()

    population = new_population
    generation += 1


print("\nNo perfect solution found within generation limit.")