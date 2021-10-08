import random
import functools
import datetime

random.seed(datetime.datetime.now())
MAX = 2^6
NUMBER_OF_CHROMOSOMES = 20
NUMBER_OF_GENES = 4

GENERATIONS = 1000


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

def func1(x, y, z, w):
  return abs(pow(x, 2) + pow(y, 3) + pow(z, 4) - pow(w, 5))

def func2(x, z, w):
  return abs(pow(x, 2) + (3 * pow(z, 2)) - w)

def func3(z, y):
  return abs(pow(z, 5) - y - 10)

def func4(x, y, z, w):
  return abs(pow(x, 4) - z + (y * w))

def breed(gene,other_gene):
  gene = gene_to_bin(gene)
  other_gene = gene_to_bin(other_gene)

  mid = len(gene)//random.randint(1,NUMBER_OF_CHROMOSOMES)
  aux = list(gene[:mid])
  aux.extend(list(other_gene[mid:]))
 
  return tuple([int(''.join(i), 2) for i in batch(aux,n=8) ])

def gene_to_bin(gene):
  return ''.join(['{0:08b}'.format(i) for i in gene])

def make_new_generation(old_generation, new_chromosomes):
  new_generation = old_generation
  new_generation.extend(new_chromosomes)

  new_generation = list(set(new_generation[:-8]))

  if len(new_generation) < NUMBER_OF_CHROMOSOMES:
      new_generation.extend(generate_random_chromosomes(qnt=NUMBER_OF_CHROMOSOMES-len(new_generation)))

  return new_generation


def select(chromosomes):
  print(chromosomes)
  errors  = {}

  for chromosome in chromosomes:
    error = calculate_error(chromosome)
    errors[chromosome] = error
    print(f"\tCHROMOSOME {chromosome} -> ERROR {error}".center(20,' '))

  errors = list(dict(sorted(errors.items(), key=lambda item: item[1])).keys())
  new_chromosomes = [breed(errors[i],errors[i+1]) for i in range(4)]

  new_generation = make_new_generation(chromosomes,new_chromosomes)
  
  print(new_generation)
  return new_generation

@functools.lru_cache(maxsize=None)
def calculate_error(chromosome):
  x, y, z, w = chromosome

  error =  func1(x, y, z, w) + func2(x, z, w) + func3(y, z) + func4(x, y, z, w)

  error = (1 / (1 + error))

  return error

  return x, y, z, w


def generate_random_chromosomes(qnt=NUMBER_OF_CHROMOSOMES):
  return [tuple(random.sample(range(0, 50), NUMBER_OF_GENES)) for i in range(qnt)]
if __name__ == "__main__":

  chromosomes = generate_random_chromosomes()

  for generation in range(GENERATIONS):

    print(f"GENERATION {generation}".center(20,'='))
    chromosomes = select(chromosomes)

  for final_chromosome in chromosomes:
    error = calculate_error(final_chromosome)

    print(f"\tCHROMOSOME {final_chromosome} -> ERROR {error}".center(20,' '))



