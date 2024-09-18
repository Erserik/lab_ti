def lzw(input_text):
    dictionary = {}
    d_i = 0
    cs = ""

    for char in input_text:
        ns = cs + char
        if ns not in dictionary:
            dictionary[ns] = d_i
            d_i += 1
        cs = char

    print("dictionary", dictionary)

    textf = []
    cs = ""

    for char in input_text:
        ns = cs + char
        if ns in dictionary:
            cs = ns
        else:
            textf.append(dictionary[cs])
            dictionary[ns] = d_i
            d_i += 1
            cs = char
    if cs:
        textf.append(dictionary[cs])

    print("cod", textf)
    print("len code", len(textf))
    print("input_text", input_text)
    print("len input_text", len(input_text))

lzw("ATGATCATGAG")
