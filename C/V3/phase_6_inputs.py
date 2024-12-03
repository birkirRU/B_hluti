import random

def generate_sequence():
    sequence = random.sample(range(1, 7), 6)
    return sequence

# Example usage
sequence = generate_sequence()
print(*sequence)
