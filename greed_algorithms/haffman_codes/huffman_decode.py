from typing import Dict


def huffman_decode(s: str, code: Dict[str, str]) -> str:
    k = 0
    result = ''
    for i in range(len(s)):
        if s[k:i+ 1] in code.keys():
            result += code[s[k:i + 1]]
            k = i + 1
    return result


def main():
    k, length = (int(x) for x in input().split())
    decoder = {}
    for _ in range(k):
        ch, encoded_ch = input().split(': ')
        decoder[encoded_ch] = ch
    encoded_s = input()
    print(huffman_decode(encoded_s, decoder))


if __name__ == '__main__':
    main()
