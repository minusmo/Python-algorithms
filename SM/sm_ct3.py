def solution(encoded, a, b):
    answer = ''
    answer = decode_string(encoded, a, b)
    return answer

def decode_string(encoded, a, b):
    decoded = []
    for encoded_char in encoded:
        decoded_char = decode_char(encoded_char, a, b)
        decoded.append(decoded_char)
    return ''.join(decoded)

def decode_char(encoded_char, a, b):
    decoded_chr = ''
    char_ord = ord(encoded_char) - 97
    for i in range(a+1):
        multiple_of_a = char_ord + 26 * i - b
        if multiple_of_a % a == 0:
            decoded_chr = chr(multiple_of_a // a + 97)
            break
    return decoded_chr


answer = solution("soma", 3, 4)
print(answer)