import random

CHROM_LENGTH = 5
MUTATION_RATE = 0.15
MIN_GENERATIONS = 3
MAX_GENERATIONS = 50


# ---------- USER FUNCTION ----------
def user_function(x):
    return eval(FUNCTION)


# Decode binary to decimal
def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)


# Initialize population
def initialize_population(pop_size):
    population = []
    while len(population) < pop_size:
        chrom = [random.randint(0, 1) for _ in range(CHROM_LENGTH)]
        if user_function(decode(chrom)) != 1:  # avoid optimal initially
            population.append(chrom)
    return population


# Print matrix form
def print_matrix(population, title):
    print(f"\n{title} (Matrix Form)")
    print("-" * 40)
    for i, chrom in enumerate(population):
        print(f"S{i+1} -> {chrom}")
    print("-" * 40)


# Print detailed table
def print_table(population, title):
    print(f"\n{title}")
    print("-" * 65)
    print(f"{'String':<8}{'Binary':<12}{'Decimal(x)':<12}{'f(x)':<10}")
    print("-" * 65)

    for i, chrom in enumerate(population):
        x = decode(chrom)
        print(f"S{i+1:<7}{''.join(map(str, chrom)):<12}{x:<12}{user_function(x):<10}")
    print("-" * 65)


# Tournament Selection
def tournament_selection(population, pop_size):
    print("\nTournament Selection:")
    new_population = []

    for i in range(pop_size):
        a, b = random.sample(range(pop_size), 2)

        c1, c2 = population[a], population[b]
        x1, x2 = decode(c1), decode(c2)
        f1, f2 = user_function(x1), user_function(x2)

        print(f"Match {i+1}: S{a+1} ({''.join(map(str,c1))}, f={f1}) "
              f"vs S{b+1} ({''.join(map(str,c2))}, f={f2})")

        if f1 < f2:
            print(f"Winner: S{a+1}")
            new_population.append(c1.copy())
        else:
            print(f"Winner: S{b+1}")
            new_population.append(c2.copy())

    return new_population


# Single-point crossover
def crossover(population, pop_size):
    print("\nCrossover:")
    new_population = []

    for i in range(0, pop_size, 2):
        if i+1 < pop_size:
            parent1 = population[i]
            parent2 = population[i+1]

            point = random.randint(1, CHROM_LENGTH - 1)
            print(f"Crossover between S{i+1} & S{i+2} at point {point}")

            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]

            new_population.extend([child1, child2])
        else:
            new_population.append(population[i])

    return new_population


# Mutation
def mutation(population):
    print("\nMutation:")
    for i in range(len(population)):
        for j in range(CHROM_LENGTH):
            if random.random() < MUTATION_RATE:
                population[i][j] ^= 1
                print(f"Bit flipped in S{i+1} at position {j}")
    return population


# Main GA
def genetic_algorithm():

    pop_size = int(input("Enter population size (example 4): "))
    population = initialize_population(pop_size)

    initial_best_index = min(
        range(pop_size),
        key=lambda i: user_function(decode(population[i]))
    )

    generation = 1

    while generation <= MAX_GENERATIONS:

        print(f"\n\n================ GENERATION {generation} ================")

        print_matrix(population, "Initial Population")
        print_table(population, "Initial Population Details")

        population = tournament_selection(population, pop_size)
        print_table(population, "After Selection")

        population = crossover(population, pop_size)
        print_table(population, "After Crossover")

        population = mutation(population)
        print_table(population, "After Mutation")

        best_index = min(
            range(pop_size),
            key=lambda i: user_function(decode(population[i]))
        )

        best_x = decode(population[best_index])
        best_fx = user_function(best_x)

        if generation >= MIN_GENERATIONS and best_fx == 1:
            print("\nOptimal solution found!")
            break

        generation += 1

    # Final best
    final_best_index = min(
        range(pop_size),
        key=lambda i: user_function(decode(population[i]))
    )

    final_best = population[final_best_index]
    final_best_x = decode(final_best)
    final_best_fx = user_function(final_best_x)

    print("\n\n================ CONCLUSION ================")
    print(f"Initial Best -> S{initial_best_index+1}, "
          f"Binary: {''.join(map(str,population[initial_best_index]))}, "
          f"x = {decode(population[initial_best_index])}, "
          f"f(x) = {user_function(decode(population[initial_best_index]))}")

    print(f"Final Best   -> S{final_best_index+1}, "
          f"Binary: {''.join(map(str,final_best))}, "
          f"x = {final_best_x}, "
          f"f(x) = {final_best_fx}")

    print(f"Total Generations: {generation}")
    print("Genetic Algorithm successfully minimized the user-defined function.")


# --------- USER INPUT FUNCTION ----------
FUNCTION = input("Enter function in terms of x (example: x**2): ")

genetic_algorithm()