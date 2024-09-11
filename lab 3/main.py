def main(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text2 = []
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        text2.append(f"{text[i]}{count}")
        i += 1
    text2 = ''.join(text2)

    print(text)
    print(text2)
    print("исход текст", len(text))
    print("кодированый текст",len(text2))

# Запуск программы
main('r1.txt')
