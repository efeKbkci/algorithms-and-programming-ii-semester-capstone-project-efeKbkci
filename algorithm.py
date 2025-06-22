def lzw_compress(text):
    """
    LZW compression algorithm.
    text: data to be compressed
    return: compressed integer data list
    """
    # Initial dictionary (ASCII chars)
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    compressed = []
    steps = []

    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            steps.append(f"Added '{wc}' -> Code: {dict_size}")
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Remaining
    if w:
        compressed.append(dictionary[w])
    
    return compressed, steps


def lzw_decompress(compressed):
    """
    LZW decompress algorithm.
    compressed: Integer code list
    return: decompressed original data
    """
    if not compressed:
        return ""
    
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    # Take the first character
    w = chr(compressed[0])
    result = w
    steps = [f"{compressed[0]} → '{w}'"]

    for k in compressed[1:]:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError(f"Invalid code: {k}")
        
        result += entry
        steps.append(f"{k} → '{entry}'")

        # New entries are added
        dictionary[dict_size] = w + entry[0]

        steps.append(f"Added new entry: {dict_size} → '{w + entry[0]}'")
        dict_size += 1
        w = entry
    
    return result, steps
