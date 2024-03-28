import random

QUEENS = 4
MAX_GENERATIONS = 100
POPULATION_SIZE = 4

# Draw Board
def draw_board(board):
  for i in range(QUEENS):
    for j in range(QUEENS):
      if board[i] == j:
        print('Q', end = ' ')
      else:
        print('.', end = ' ')
    print()
  print()

#actual fitness score of a board with N QUEENS ( Number of Attacking Pairs )
def best_fitness():
  return (QUEENS * (QUEENS - 1) // 2)

# Fitness Score ( Number of Non-Attacking Pairs )
def fitness(board):
  score = 0
  for i in range(QUEENS): 
    for j in range(i + 1, QUEENS): # i+1 cuz we don't want to compare the same queen again
      if board[i] != board[j] and abs(board[i] - board[j]) != j - i: # if they are not in the same line and not in the same diagonal
        score += 1
  return score

# Crossover
def crossover(board1, board2):
  # Randomly select a crossover point
  crossover_point = random.randint(0, QUEENS - 1)
  new_board = board1[:crossover_point] + board2[crossover_point:]
  new_board2 = board2[:crossover_point] + board1[crossover_point:]
  return new_board, new_board2

# Mutation
def mutation(board1, board2):
  # Randomly select a mutation point
  mutation_point = random.randint(0, QUEENS - 1)
  new_board1 = board1[:] # copying board1 into new_board
  new_board1[mutation_point] = random.randint(0, QUEENS - 1)
  new_board2 = board2[:]
  new_board2[mutation_point] = random.randint(0, QUEENS - 1)
  return new_board1, new_board2

def generate_population():
  p = []
  for i in range(POPULATION_SIZE):
    board = [random.randint(0, QUEENS - 1) for j in range(QUEENS)]
    p.append(board)
  return p

def generate_new_population(Population):
  # Generate new population
  new_population = Population[:]
  # Selecting two boards from the population based on fitness
  board1 = random.choices(Population, weights = [fitness(board) for board in Population])[0]
  # To avoid selecting the same board twice
  Population_without_board1 = [board for board in Population if board != board1]
  if Population_without_board1:
    weights = [fitness(board) for board in Population_without_board1]
    if sum(weights) > 0:
      board2 = random.choices(Population_without_board1, weights=weights)[0]
    else:
      # If all weights are zero, select board2 randomly without considering the weights
      board2 = random.choice(Population_without_board1)
  else:
    # Case where all boards in Population are equal to board1
    raise ValueError("All boards in Population are the same")

  new_population.remove(board1)
  new_population.remove(board2)
  print("Choosing:  ",board1, fitness(board1), board2, fitness(board2))
  # Crossover
  new_board, new_board2 = crossover(board1, board2)
  print("Crossover: ", new_board, fitness(new_board), new_board2, fitness(new_board2))
  # Mutation
  if random.random() < 0.5:
    new_board, new_board2 = mutation(new_board, new_board2)
    print("Mutation:  ", new_board, fitness(new_board), new_board2, fitness(new_board2))
  # Replace board1 and board2 with new_board and new_board2
  new_population.append(new_board)
  new_population.append(new_board2)
  return new_population

def eight_queens_problem(Population):
  # Number of generations
  for i in range(MAX_GENERATIONS):
    for board in Population:
      #print(fitness(board))
      if fitness(board) == best_fitness():
        print("\nSolution Found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        draw_board(board)
        return board
    Population = generate_new_population(Population)
    print("Generation: ", i)
    print(Population)
  return "\nNo Solution Found"

# Generating Initial Population
Population = generate_population()
print(Population)
print(eight_queens_problem(Population), "with a fitness of",best_fitness(), end='\n\n')

