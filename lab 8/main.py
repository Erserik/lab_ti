class LZ77:
    def __init__(self, search_window_size, buffer_size):
        self.search_window_size = search_window_size
        self.buffer_size = buffer_size

    def encode(self, input_string):
        encoded_output = []
        i = 0

        while i < len(input_string):
            match_offset = 0
            match_length = 0
            next_char = input_string[i]

            start_index = max(0, i - self.search_window_size)
            search_window = input_string[start_index:i]
            buffer = input_string[i:i + self.buffer_size]

            for j in range(len(search_window)):
                substring = search_window[j:]
                match_len = 0
                while match_len < len(buffer) and match_len < len(substring) and buffer[match_len] == substring[
                    match_len]:
                    match_len += 1
                if match_len > match_length:
                    match_length = match_len
                    match_offset = len(search_window) - j

            if match_length > 0:
                next_char = buffer[match_length] if match_length < len(buffer) else ''

            encoded_output.append((match_offset, match_length, next_char))
            i += match_length + 1

        return encoded_output

    def decode(self, encoded_data):
        decoded_output = []

        for offset, length, next_char in encoded_data:
            start_index = len(decoded_output) - offset
            for _ in range(length):
                decoded_output.append(decoded_output[start_index])
                start_index += 1
            if next_char:
                decoded_output.append(next_char)

        return ''.join(decoded_output)


if __name__ == "__main__":
    search_window_size = 5
    buffer_size = 3
    test_string = "ABABABAB"

    print("Исходный текст:", test_string)

    lz77 = LZ77(search_window_size=search_window_size, buffer_size=buffer_size)

    encoded = lz77.encode(test_string)
    print("Закодировано:", encoded)

    decoded = lz77.decode(encoded)
    print("Декодированный текст:", decoded)

    if test_string == decoded:
        print("Успешно: исходная строка совпадает с декодированной.")
    else:
        print("Ошибка: строки не совпадают!")
