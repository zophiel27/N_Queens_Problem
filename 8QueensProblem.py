import random
# Draw Board
def draw_board(board):
  for i in range(8):
    for j in range(8):
      if board[i] == j:
        print('Q', end = ' ')
      else:
        print('.', end = ' ')
    print()
  print()

# Fitness Score ( Number of Non-Attacking Pairs )
def fitness(board):
  # Highest fitness score (i.e. best solution) is 27 in this case
  score = 0
  for i in range(8):
    attacking_queens = 0
    for j in range(i+1, 8): # i+1 cuz we don't want to compare the same queen again
      if board[i] == board[j]:
        attacking_queens += 1
      if abs(board[i] - board[j]) == j - i:
        attacking_queens += 1
    non_attacking_queens = 7 - i - attacking_queens
    score += non_attacking_queens 
  return score

# Crossover
def crossover(board1, board2):
  # Randomly select a crossover point
  crossover_point = random.randint(0, 7)
  new_board = board1[:crossover_point] + board2[crossover_point:]
  new_board2 = board2[:crossover_point] + board1[crossover_point:]
  return new_board, new_board2

# Mutation
def mutation(board, board2):
  # Randomly select a mutation point
  mutation_point = random.randint(0, 7)
  new_board = board[:] # copying board into new_board
  new_board[mutation_point] = random.randint(0, 7)
  new_board2 = board2[:]
  new_board2[mutation_point] = random.randint(0, 7)
  return new_board, new_board2

def generate_population(Population, P):
  # Generate new population
  new_population = Population[:]
  # Selecting two boards from the population based on fitness
  board1 = random.choices(Population, weights = [fitness(board) for board in Population])[0]
  board2 = board1
  # making sure board2 is different from board1
  while board2 == board1:
    board2 = random.choices(Population, weights = [fitness(board) for board in Population])[0]
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

def eight_queens_problem(Population, P):
  # Number of generations
  G = 100
  for i in range(G):
    for board in Population:
      #draw_board(board)
      print(fitness(board))
      if fitness(board) == 27:
        print("Solution Found!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return board
    Population = generate_population(Population, P)
    print("Generation: ", i)
    print(Population)
  return "No Solution Found"
  


# Generating Initial Population
P = 10
Population = []
for i in range(P):
  board = [random.randint(0, 7) for j in range(8)]
  Population.append(board)
print(Population)
print(eight_queens_problem(Population, P))
