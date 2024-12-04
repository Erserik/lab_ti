def crc_calculation(data, generator):
    # Преобразуем строки данных и полинома в списки целых чисел
    data = [int(bit) for bit in data]
    generator = [int(bit) for bit in generator]

    # Добавляем нули в конец данных (длина генератора - 1)
    data.extend([0] * (len(generator) - 1))

    # Копируем данные для изменения в процессе деления
    remainder = data[:]

    # Длина генератора
    generator_len = len(generator)

    # Побитное деление (XOR)
    for i in range(len(data) - generator_len + 1):
        if remainder[i] == 1:  # Если текущий бит равен 1, выполняем XOR
            for j in range(generator_len):
                remainder[i + j] ^= generator[j]  # Побитовое XOR

    # Остаток (CRC) — последние (длина генератора - 1) бита
    crc = remainder[-(generator_len - 1):]
    return crc


def crc_check(data_with_crc, generator):
    # Преобразуем строки в списки целых чисел
    data_with_crc = [int(bit) for bit in data_with_crc]
    generator = [int(bit) for bit in generator]

    # Копируем данные для изменения
    remainder = data_with_crc[:]

    # Длина генератора
    generator_len = len(generator)

    # Побитное деление (XOR)
    for i in range(len(data_with_crc) - generator_len + 1):
        if remainder[i] == 1:  # Если текущий бит равен 1, выполняем XOR
            for j in range(generator_len):
                remainder[i + j] ^= generator[j]  # Побитовое XOR

    # Остаток (должен быть нулевым, если данные переданы без ошибок)
    return all(bit == 0 for bit in remainder[-(generator_len - 1):])


# Пример использования
data = "11010011"  # Исходные данные
generator = "10011"  # Генераторный полином

# Вычисление CRC
crc = crc_calculation(data, generator)
print("CRC-код:", "".join(map(str, crc)))

# Добавление CRC к данным
data_with_crc = data + "".join(map(str, crc))
print("Данные с CRC:", data_with_crc)

# Проверка данных с CRC
is_valid = crc_check(data_with_crc, generator)
print("Данные корректны?", "Да" if is_valid else "Нет")

# Имитация ошибки
data_with_error = list(data_with_crc)
data_with_error[5] = '1' if data_with_crc[5] == '0' else '0'  # Изменяем один бит
data_with_error = "".join(data_with_error)

print("Данные с ошибкой:", data_with_error)
is_valid_error = crc_check(data_with_error, generator)
print("Данные корректны?", "Да" if is_valid_error else "Нет")
