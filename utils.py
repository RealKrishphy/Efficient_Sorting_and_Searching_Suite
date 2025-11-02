import random
def generate_dataset(size):
random.seed()
return [random.randint(1, 1000) for _ in range(size)]
