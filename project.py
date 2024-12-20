import random
def fitness_function(x):
    return x ** 2
def generate_population(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

def select_parents(population):
    fitnesses = [fitness_function(x) for x in population]
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 1)
    if crossover_point == 0:
        return parent1, parent2
    else:
        return parent2, parent1
def mutate(child, lower_bound, upper_bound, mutation_rate=0.1):
    if random.random() < mutation_rate:
        child += random.choice([-1, 1])
        child = max(lower_bound, min(upper_bound, child))
    return child

def genetic_algorithm(generations, population_size, lower_bound, upper_bound):

    population = generate_population(population_size, lower_bound, upper_bound)
    
    for generation in range(generations):

        population = sorted(population, key=fitness_function, reverse=True)
        best_individual = population[0]
        print(f"Generation {generation}: Best Individual = {best_individual}, Fitness = {fitness_function(best_individual)}")

        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, lower_bound, upper_bound)
            child2 = mutate(child2, lower_bound, upper_bound)
            next_generation.extend([child1, child2])
        
        population = next_generation

    population = sorted(population, key=fitness_function, reverse=True)
    best_solution = population[0]
    print(f"\nBest solution after {generations} generations: {best_solution}, Fitness = {fitness_function(best_solution)}")
genetic_algorithm(generations=20, population_size=10, lower_bound=-10, upper_bound=10)
