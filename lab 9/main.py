def calculate_check_bits_length(data_length):
    r = 0
    while (2 ** r) < (data_length + r + 1):
        r += 1
    return r

def encode_hamming(data):
    data_length = len(data)
    r = calculate_check_bits_length(data_length)
    total_length = data_length + r

    hamming_code = ['0'] * total_length
    j = 0

    for i in range(1, total_length + 1):
        if (i & (i - 1)) == 0:
            continue
        hamming_code[i - 1] = data[j]
        j += 1

    for i in range(r):
        check_pos = 2 ** i
        parity = 0
        for j in range(1, total_length + 1):
            if j & check_pos and hamming_code[j - 1] == '1':
                parity ^= 1
        hamming_code[check_pos - 1] = str(parity)

    return ''.join(hamming_code)

def detect_and_correct_error(hamming_code):
    total_length = len(hamming_code)
    r = calculate_check_bits_length(total_length - sum(1 for i in range(total_length) if (i + 1 & i) == 0))
    error_pos = 0

    for i in range(r):
        check_pos = 2 ** i
        parity = 0
        for j in range(1, total_length + 1):
            if j & check_pos and hamming_code[j - 1] == '1':
                parity ^= 1
        if parity != 0:
            error_pos += check_pos

    if error_pos > 0:
        error_index = error_pos - 1
        hamming_code = list(hamming_code)
        hamming_code[error_index] = '1' if hamming_code[error_index] == '0' else '0'

    return ''.join(hamming_code), error_pos

def extract_original_message(hamming_code):
    original_message = []
    for i in range(1, len(hamming_code) + 1):
        if (i & (i - 1)) != 0:
            original_message.append(hamming_code[i - 1])
    return ''.join(original_message)

if __name__ == "__main__":
    original_data = "1011"
    print("Исходное сообщение:", original_data)

    encoded_message = encode_hamming(original_data)
    print("Закодированное сообщение (код Хэмминга):", encoded_message)

    encoded_message_with_error = list(encoded_message)
    encoded_message_with_error[3] = '1' if encoded_message_with_error[3] == '0' else '0'
    encoded_message_with_error = ''.join(encoded_message_with_error)
    print("Сообщение с ошибкой:", encoded_message_with_error)

    corrected_message, error_position = detect_and_correct_error(encoded_message_with_error)
    print("Исправленное сообщение:", corrected_message)
    print("Позиция ошибки:", error_position)

    recovered_message = extract_original_message(corrected_message)
    print("Восстановленное исходное сообщение:", recovered_message)
