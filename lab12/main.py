def calculate_crc(data: str, generator: str) -> str:
    """Вычисляет CRC-код для заданных данных и генератора."""
    data_bits = [int(bit) for bit in data]
    generator_bits = [int(bit) for bit in generator]
    data_bits += [0] * (len(generator_bits) - 1)

    for i in range(len(data_bits) - len(generator_bits) + 1):
        if data_bits[i] == 1:
            for j in range(len(generator_bits)):
                data_bits[i + j] ^= generator_bits[j]

    return ''.join(map(str, data_bits[-(len(generator_bits) - 1):]))


def verify_crc(data_with_crc: str, generator: str) -> bool:
    """Проверяет данные с CRC-кодом на корректность."""
    data_bits = [int(bit) for bit in data_with_crc]
    generator_bits = [int(bit) for bit in generator]

    for i in range(len(data_bits) - len(generator_bits) + 1):
        if data_bits[i] == 1:
            for j in range(len(generator_bits)):
                data_bits[i + j] ^= generator_bits[j]

    remainder = data_bits[-(len(generator_bits) - 1):]
    return all(bit == 0 for bit in remainder)


def main():
    data = "11010011"
    generator = "10011"

    crc = calculate_crc(data, generator)
    print(f"CRC-код: {crc}")

    data_with_crc = data + crc
    print(f"Данные с CRC: {data_with_crc}")
    is_valid = verify_crc(data_with_crc, generator)
    print(f"Проверка данных: {'Данные корректны' if is_valid else 'Обнаружена ошибка'}")

    data_with_error = data_with_crc[:3] + ('1' if data_with_crc[3] == '0' else '0') + data_with_crc[4:]
    print(f"Данные с ошибкой: {data_with_error}")
    is_valid_error = verify_crc(data_with_error, generator)
    print(f"Проверка данных с ошибкой: {'Данные корректны' if is_valid_error else 'Обнаружена ошибка'}")


if __name__ == "__main__":
    main()
