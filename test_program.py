from Biblioteki import Core


def test_huffman1():
    coding = Core.huffman_encode(Core.prepare_chars("Data/test1.txt"))
    encoded = Core.encode_word("SEKRET", coding)
    assert encoded == "00110100111110"
