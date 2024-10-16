def calc_freq(s):
    f = {}
    for c in s:
        f[c] = f.get(c, 0) + 1
    total = len(s)
    return {c: freq / total for c, freq in f.items()}

def encode(s):
    f = calc_freq(s)
    lo, hi = 0.0, 1.0
    for c in s:
        r = hi - lo
        hi = lo + r * (f[c] + sum(f[cc] for cc in f if cc < c))
        lo = lo + r * sum(f[cc] for cc in f if cc < c)
    return (lo + hi) / 2

s = 'hello'
f = calc_freq(s)
print(encode(s))
