import numpy as np

# Порождающая матрица (G)
G = np.array([
    [1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1]
])

# Проверочная матрица (H)
H = np.array([
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 1]
])

def encode_message(m, G):
    return np.dot(m, G) % 2

def detect_error(c, H):
    return np.dot(c, H.T) % 2

def correct_error(c, syndrome, H):
    for i in range(H.shape[1]):
        if np.array_equal(H[:, i], syndrome):
            c[i] = 1 - c[i]
            break
    return c

messages = [
    np.array([1, 0, 1]),
    np.array([0, 1, 1]),
    np.array([1, 1, 0])
]

print("Кодирование сообщений:")
codewords = []
for m in messages:
    c = encode_message(m, G)
    codewords.append(c)
    print(f"Сообщение: {m}, Кодовое слово: {c}")

# Имитация ошибки
print("\nОбнаружение и исправление ошибок:")
received = codewords[0].copy()
received[1] = 1 - received[1]  # Ошибка во 2-м бите

print(f"Принятое (с ошибкой): {received}")
syndrome = detect_error(received, H)
print(f"Синдром ошибки: {syndrome}")

if np.any(syndrome):
    corrected = correct_error(received, syndrome, H)
    print(f"Исправленное кодовое слово: {corrected}")
else:
    print("Ошибок не обнаружено.")
