import random
import string
from collections import Counter
import math

s = list(string.ascii_letters)
with open('../lab 2/r1.txt', 'w') as file:
    random_string = ''.join(random.choices(s, k=2000))
    file.write(random_string)

b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
with open('../lab 2/r2.txt', 'w') as file:
    random_digits = ''.join(random.choices(b, k=2000))
    file.write(random_digits)

counter_r1 = Counter(random_string)
counter_r2 = Counter(random_digits)

prob_r1 = {char: count/len(random_string) for char, count in counter_r1.items()}
prob_r2 = {char: count/len(random_digits) for char, count in counter_r2.items()}

en_r1 = {char: prob * math.log2(prob) for char, prob in prob_r1.items()}
en_r2 = {char: prob * math.log2(prob) for char, prob in prob_r2.items()}

print("r1:", counter_r1)
print("r1:", prob_r1)
print("P(xi) * log2(P(xi)) r1:", en_r1)
print("sum P(xi) * log2(P(xi)) r1:", sum(en_r1.values()))

print("r2:", counter_r2)
print("r2:", prob_r2)
print("P(xi) * log2(P(xi)) r2:", en_r2)
print("sum P(xi) * log2(P(xi)) r2:", sum(en_r2.values()))