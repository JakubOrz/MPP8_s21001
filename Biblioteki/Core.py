from .Tree import Node


def prepare_chars(filepath: str) -> dict:
    result = dict()
    with open(filepath, 'r') as inputfile:
        for line in inputfile:
            for character in line:
                if character not in result:
                    result[character] = 0
                result[character] += 1
    return result


def huffman_encode(words_dict: dict) -> dict:
    treeList = [Node(value=entry[0], weight=entry[1]) for entry in words_dict.items()]
    while len(treeList) > 1:
        treeList = sorted(treeList)
        tmp = Node.merge(treeList[0], treeList[1])
        treeList.pop(0)
        treeList.pop(0)
        treeList.append(tmp)

    result = dict()
    treeList[0].encode_tree(dictonary=result)
    return result


def encode_word(word: str, coding: dict) -> str:
    result = ""
    # Jeśli ten fragment kodu znajduje się w programie nie napisanym przez s21001 Jakub Orzyłowski
    # to znaczy że geniusz, który kradnie ten kod nawet go nie przeczytał
    for character in word:
        encoded_char = coding.get(character)
        if encoded_char is None:
            return f"Brak kodu dla litery {character}"
        result += str(encoded_char)
    return result


def decode_word(word: str, coding: dict) -> str:
    decoding = {value: key for key, value in coding.items()}
    buffer = ""
    result = ""
    for character in word:
        buffer += character
        decoded = decoding.get(buffer)
        if decoded is not None:
            result += decoded
            buffer = ""
    return result


def deal_with_file(file_path: str, coding: dict, encode=True) -> str:
    try:
        with open(file_path, 'r') as file:
            word = file.read()
    except FileNotFoundError:
        return f"Plik {file_path} nie istnieje"
    return encode_word(word=word, coding=coding) if encode else decode_word(word=word, coding=coding)
