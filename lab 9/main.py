def calculate_check_bits_length(data_length):
    # Вычисляем количество контрольных битов (r), необходимых для кодирования сообщения
    r = 0
    # Условие: 2^r >= data_length + r + 1
    while (2 ** r) < (data_length + r + 1):
        r += 1
    return r  # Возвращаем количество контрольных битов


def encode_hamming(data):
    # Определяем длину исходных данных
    data_length = len(data)
    # Вычисляем количество контрольных битов
    r = calculate_check_bits_length(data_length)
    # Общая длина сообщения (данные + контрольные биты)
    total_length = data_length + r

    # Создаём массив для закодированного сообщения
    hamming_code = ['0'] * total_length
    j = 0  # Индекс для исходных данных

    # Распределяем исходные данные в массив с учётом позиций контрольных битов
    for i in range(1, total_length + 1):
        # Позиции, равные степеням двойки (1, 2, 4, 8...), оставляем для контрольных битов
        if (i & (i - 1)) == 0:  # Проверка, является ли i степенью двойки
            continue
        hamming_code[i - 1] = data[j]  # Записываем данные
        j += 1

    # Вычисляем значения контрольных битов
    for i in range(r):
        check_pos = 2 ** i  # Позиция контрольного бита (1, 2, 4, ...)
        parity = 0  # Начальное значение контрольного бита
        for j in range(1, total_length + 1):
            # Если бит участвует в проверке контрольного бита
            if j & check_pos and hamming_code[j - 1] == '1':
                parity ^= 1  # Считаем чётность
        hamming_code[check_pos - 1] = str(parity)  # Устанавливаем значение контрольного бита

    return ''.join(hamming_code)  # Возвращаем закодированное сообщение


def detect_and_correct_error(hamming_code):
    # Определяем длину сообщения
    total_length = len(hamming_code)
    # Вычисляем количество контрольных битов
    r = calculate_check_bits_length(total_length - sum(1 for i in range(total_length) if (i + 1 & i) == 0))
    error_pos = 0  # Переменная для хранения позиции ошибки

    # Проверяем все контрольные биты
    for i in range(r):
        check_pos = 2 ** i  # Позиция контрольного бита
        parity = 0  # Значение текущего контрольного бита
        for j in range(1, total_length + 1):
            # Если бит участвует в проверке контрольного бита
            if j & check_pos and hamming_code[j - 1] == '1':
                parity ^= 1  # Считаем чётность
        if parity != 0:  # Если есть несоответствие
            error_pos += check_pos  # Добавляем позицию в номер ошибки

    # Если ошибка найдена, исправляем её
    if error_pos > 0:
        error_index = error_pos - 1  # Индекс ошибки (0-основанный)
        hamming_code = list(hamming_code)  # Преобразуем строку в список для изменения
        # Переворачиваем бит (0 -> 1, 1 -> 0)
        hamming_code[error_index] = '1' if hamming_code[error_index] == '0' else '0'

    return ''.join(hamming_code), error_pos  # Возвращаем исправленное сообщение и позицию ошибки


def extract_original_message(hamming_code):
    # Извлекаем исходное сообщение (убираем контрольные биты)
    original_message = []
    for i in range(1, len(hamming_code) + 1):
        # Пропускаем позиции контрольных битов (степени двойки)
        if (i & (i - 1)) != 0:
            original_message.append(hamming_code[i - 1])  # Добавляем бит в результат
    return ''.join(original_message)  # Возвращаем исходное сообщение


if __name__ == "__main__":
    # Исходные данные
    original_data = "1011"
    print("Исходное сообщение:", original_data)

    # Кодируем сообщение с использованием кода Хэмминга
    encoded_message = encode_hamming(original_data)
    print("Закодированное сообщение (код Хэмминга):", encoded_message)

    # Добавляем ошибку в сообщение (например, меняем 4-й бит)
    encoded_message_with_error = list(encoded_message)
    encoded_message_with_error[3] = '1' if encoded_message_with_error[3] == '0' else '0'
    encoded_message_with_error = ''.join(encoded_message_with_error)
    print("Сообщение с ошибкой:", encoded_message_with_error)

    # Обнаруживаем и исправляем ошибку
    corrected_message, error_position = detect_and_correct_error(encoded_message_with_error)
    print("Исправленное сообщение:", corrected_message)
    print("Позиция ошибки:", error_position)

    # Извлекаем исходное сообщение из исправленного
    recovered_message = extract_original_message(corrected_message)
    print("Восстановленное исходное сообщение:", recovered_message)
