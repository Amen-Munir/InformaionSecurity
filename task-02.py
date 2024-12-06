import random

class Gene:
    def __init__(self, gene: str = "", fitness: int = 0, fitnessRatio: float = 0.0, commualativeFitness: float = 0.0,selectedd: str = "NO"):
        self.gene = gene
        self.fitness = fitness
        self.fitnessRatio = fitnessRatio
        self.commualativeFitness = commualativeFitness
        self.selectedd = selectedd

    def __repr__(self):
        return f"Gene(gene='{self.gene}', fitness={self.fitness}, fitnessRatio={self.fitnessRatio}, commualativeFitness={self.commualativeFitness})"

populationSize = 10
lengthOfEachString = 4


def generatePop():
    population = []
    for _ in range(populationSize):
        gene_string = ''.join(random.choice(['0', '1']) for _ in range(lengthOfEachString))
        population.append(Gene(gene=gene_string))
    return population


def fitnessFunction(population):
    for individual in population:
        individual.fitness = round(random.uniform(0, 30),2)  
    return population



def rankPop(population):
    return sorted(population, key=lambda x: x.fitness, reverse=True)


def calculateFitnessRatio(population):
    totalFitness = sum(individual.fitness for individual in population)
    for individual in population:
        individual.fitnessRatio = round(individual.fitness / totalFitness, 3) * 100
    return population


def calculateCumulativeFitness(population):
    cumulative = 0
    for individual in population:
        cumulative += individual.fitnessRatio
        individual.commualativeFitness = cumulative
    return population



def rouletteWheelSelection(population):
    r = random.uniform(0, 100)  
    print(f"Random Number: {r}")
    for individual in population:
        if r <= individual.commualativeFitness:
            individual.selectedd = "YES"
            return individual

def crossover(parent1,parent2):
    r = int(random.uniform(0,4) )
    print(f"Random Number: {r}")
    child1=parent1.gene[:r]+parent2.gene[r:]
    child2=parent2.gene[:r]+parent1.gene[r:]
    return child1,child2



def mutation(c1):
    r = random.randint(0, lengthOfEachString - 1)
    c1 = list(c1)  
    c1[r] = '0' if c1[r] == '1' else '1'
    return ''.join(c1)  


Population = generatePop()
Population = fitnessFunction(Population)
Population = rankPop(Population)
Population = calculateFitnessRatio(Population)
Population = calculateCumulativeFitness(Population)




parent1 = rouletteWheelSelection(Population)




for i in range(populationSize):
    print(" ")
    print(f'Individual:{Population[i].gene}, fitness(yield): {Population[i].fitness},Ration: {Population[i].fitnessRatio},Commulative Fitness: {Population[i].commualativeFitness}, Selected: {Population[i].selectedd}')    

# c1,c2=crossover(parent1,parent2)
# print(f"\nChild 1: {c1}")
# print(f"\nChild 2: {c2}")
# c1=mutation(c1)
# c2=mutation(c2)
# print(f"\nMutated Child 1: {c1}")
# print(f"\nMutated Child 2: {c2}")