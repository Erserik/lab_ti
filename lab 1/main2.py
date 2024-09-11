from collections import Counter
import math
import matplotlib.pyplot as plt


def calculate_entropy(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    text = ''.join(char for char in text if char.isprintable())

    counter = Counter(text)
    prob = {char: count / len(text) for char, count in counter.items()}
    entropy_values = {char: prob_value * math.log2(prob_value) for char, prob_value in prob.items()}
    iz = ((math.log2(len(prob)) - (-sum(entropy_values.values()))) / math.log2(len(prob))) * 100

    print("Count: ", counter)
    print("Probabilities: ", prob)
    print("P(xi) * log2(P(xi)): ", entropy_values)
    print("Sum P(xi) * log2(P(xi)): ", (-sum(entropy_values.values())))
    print("Избыточность: ", iz)

    plt.bar(prob.keys(), prob.values())
    plt.xlabel('Characters')
    plt.ylabel('Probability')
    plt.show()


calculate_entropy('../lab 2/r6.txt')
