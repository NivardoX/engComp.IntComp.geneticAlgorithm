import random
import functools
import datetime

random.seed(datetime.datetime.now())
MAX = 2^4
NUMBER_OF_CROMOSSOMES = 6
GENERATIONS = 10

def func1(x, y, z, w):
  return abs(pow(x, 2) + pow(y, 3) + pow(z, 4) - pow(w, 5))

def func2(x, z, w):
  return abs(pow(x, 2) + (3 * pow(z, 2)) - w)

def func3(z, y):
  return abs(pow(z, 5) - y - 10)

def func4(x, y, z, w):
  return abs(pow(x, 4) - z + (y * w))

def breed(gene,other_gene):
  mid = len(gene)//2
  return f"{gene[:mid]}{other_gene[mid:]}"

def gene_to_bin(gene):
  pass

def select(cromossomes):
  print(cromossomes)
  errors  = {}
  for cromossome in cromossomes:
    error = calculate_error(cromossome)
    errors[cromossome] = error
    print(f"\tCROMOSSOME {cromossome} -> ERROR {error}".center(20,' '))

  errors = list(dict(sorted(errors.items(), key=lambda item: item[1])).keys())
  print(errors)
  new_cromossome = breed(errors[0],errors[1])
  errors.pop(-1)

  new_generation = [error for error in errors]
  new_generation.append(new_cromossome)
  
  print(new_generation)
  return new_generation

@functools.lru_cache(maxsize=None)
def calculate_error(cromossome):
  x, y, z, w = [int(gene) for gene in cromossome]

  error =  func1(x, y, z, w) + func2(x, z, w) + func3(y, z) + func4(x, y, z, w)

  error = (1 / (1 + error))

  return error

def setVariables(vetor):
  x = vetor[0]
  y = vetor[1]
  z = vetor[2]
  w = vetor[3]

  return x, y, z, w

if __name__ == "__main__":

  cromossomes = ['{0:04b}'.format(i) for i in random.sample(range(0, MAX), NUMBER_OF_CROMOSSOMES)]

  for generation in range(GENERATIONS):

    print(f"GENERATION {generation}".center(20,'='))
    cromossomes = select(cromossomes)

  for final_cromossome in cromossomes:
    error = calculate_error(final_cromossome)

    print(f"\tCROMOSSOME {final_cromossome} -> ERROR {error}".center(20,' '))



