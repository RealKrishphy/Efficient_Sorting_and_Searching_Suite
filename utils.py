import random

def generate_dataset(size):
    random.seed()
    if size <= 50:
        return [random.randint(1, 100) for _ in range(size)]
    elif size <= 200:
        return [random.randint(1, 500) for _ in range(size)]
    else:
        return [random.randint(1, 1000) for _ in range(size)]

def get_hardcoded_dataset():
    return [
        423, 87, 612, 145, 789, 234, 901, 456, 78, 345,
        567, 890, 123, 456, 789, 234, 567, 890, 123, 456,
        789, 234, 567, 890, 123, 456, 789, 234, 567, 890,
        123, 456, 789, 234, 567, 890, 123, 456, 789, 234,
        567, 890, 123, 456, 789, 234, 567, 890, 123, 456
    ]
