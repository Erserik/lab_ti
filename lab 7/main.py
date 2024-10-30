from collections import Counter
def calculate(data):
    frequency = Counter(data)
    total_symbols = len(data)
    probabilities = {char: count / total_symbols for char, count in frequency.items()}
    return sorted(probabilities.items(), key=lambda x: x[1], reverse=True)


def shannon_fano_coding(symbols, prefix=''):
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}

    total_prob = sum(prob for _, prob in symbols)
    cumulative_prob = 0
    split_index = 0
    for i, (_, prob) in enumerate(symbols):
        cumulative_prob += prob
        if cumulative_prob >= total_prob / 2:
            split_index = i + 1
            break

    left_group = symbols[:split_index]
    right_group = symbols[split_index:]

    code = {}
    code.update(shannon_fano_coding(left_group, prefix + '0'))
    code.update(shannon_fano_coding(right_group, prefix + '1'))
    return code


message = "ABCABEAAFB"
symbols = calculate("ABCABEAAFB")
print(symbols)
code_map = shannon_fano_coding(symbols)
print(code_map)
encoded_message = ''.join(code_map[char] for char in message)
print(encoded_message)
