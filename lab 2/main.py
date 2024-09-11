from collections import Counter
import math
import matplotlib.pyplot as plt


def calculate(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    text = ''.join(char for char in text if char.isprintable())

    pairs = [(text[i], text[i + 1]) for i in range(len(text) - 1)]
    print("pairs: ", pairs)
    pair_counts = Counter(pairs)
    print("pair_counts: ", pair_counts)
    total_pairs = sum(pair_counts.values())
    print("total_pairs: ", total_pairs)

    pair_probabilities = {pair: count / total_pairs for pair, count in pair_counts.items()}

    entropy = -sum(prob * math.log2(prob) for prob in pair_probabilities.values())

    print("Энтропия: ",entropy )


    plt.figure(figsize=(100, 6))
    plt.bar(range(len(list(pair_counts.keys()))), list(pair_counts.values()), tick_label=[f"{p[0]}{p[1]}" for p in list(pair_counts.keys())])
    plt.xlabel('Пары символов')
    plt.ylabel('Частота')
    plt.tight_layout()
    plt.show()


calculate('r3.txt')
