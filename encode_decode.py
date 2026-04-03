# https://prachub.com/interview-questions/implement-run-length-encoding-and-decoding
from tokenize import endpats


def encode(text):

    start = 0
    end = 0
    last_char = text[0]
    texts = []
    while end < len(text):
        char = text[end]
        if char == last_char:
            end += 1
        else:
            texts.append(last_char)
            texts.append(str(end-start))
            last_char = char
            start = end
            end = end + 1
    texts.append(last_char)
    texts.append(str(end - start))
    return "".join(texts)

def decode(text):

    decoded = []

    for i in range(0, len(text), 2):
        char = text[i]
        count = text[i+1]
        decoded.append(char * int(count))
    return "".join(decoded)

if __name__ == "__main__":
    original = "aaabccccd"
    encoded = encode(original)
    "a3b1c4d1"
    decoded = decode(encoded)
    print(encoded)
    print(decoded)# "aaabccccd"




