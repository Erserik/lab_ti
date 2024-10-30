from collections import Counter


def calc_probs(data):
    freq = Counter(data)
    total = len(data)
    probs = {char: count / total for char, count in freq.items()}
    return sorted(probs.items(), key=lambda x: x[1], reverse=True)


def shannon_fano(symbols, prefix=''):
    if len(symbols) == 1:
        return {symbols[0][0]: prefix}

    total_prob = sum(prob for _, prob in symbols)
    cum_prob = 0
    split_idx = 0
    for i, (_, prob) in enumerate(symbols):
        cum_prob += prob
        if cum_prob >= total_prob / 2:
            split_idx = i + 1
            break

    left = symbols[:split_idx]
    right = symbols[split_idx:]

    code = {}
    code.update(shannon_fano(left, prefix + '0'))
    code.update(shannon_fano(right, prefix + '1'))
    return code


msg = "ABCABEAAFB"
symbols = calc_probs(msg)
print(symbols)
code_map = shannon_fano(symbols)
print(code_map)
encoded_msg = ''.join(code_map[char] for char in msg)
print(encoded_msg)
