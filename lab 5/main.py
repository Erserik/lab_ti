from collections import defaultdict
def hft(s):
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1

    nodes = []
    for ch in freq:
        nodes.append([freq[ch], [ch, ""]])
    print(nodes)
    nodes.sort()

    while len(nodes) > 1:
        lo = nodes.pop(0)
        hi = nodes.pop(0)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        new_node = [lo[0] + hi[0]] + lo[1:] + hi[1:]
        nodes.append(new_node)

        nodes.sort()

    result = nodes[0][1:]
    print("r", result)
    return result


def huffman_encode(s):
    huff_tree = hft(s)

    huff_dict = {}
    for ch, code in huff_tree:
        huff_dict[ch] = code

    et = ""
    for ch in s:
        et += huff_dict[ch]

    return et


print("Закодированный текст:", huffman_encode("aabacdb"))

