import heapq
from collections import Counter, namedtuple
from typing import Dict


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code: Dict[str, str], acc: str) -> None:
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code: Dict[str, str], acc: str) -> None:
        code[self.char] = acc or '0'


def huffman_encode(s: str) -> Dict[str, str]:
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, count1, left = heapq.heappop(h)
        freq2, count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_, _, root)] = h
        root.walk(code, '')
    return code


def main() -> None:
    s = input()
    code = huffman_encode(s)
    encoded = ''.join([code[ch] for ch in s])
    print(len(code.keys()), len(encoded))
    for ch in code.keys():
        s1 = f'{ch}: {code[ch]}'
        print(s1)
    print(encoded)


if __name__ == '__main__':
    main()
