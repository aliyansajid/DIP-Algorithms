import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, frequency, symbol=None, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(frequency_dict):
    priority_queue = [HuffmanNode(frequency, symbol) for symbol, frequency in frequency_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(left.frequency + right.frequency, left=left, right=right)
        heapq.heappush(priority_queue, merged)

    return heapq.heappop(priority_queue)

def build_huffman_codes(tree, prefix="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if tree.symbol is not None:
        code_dict[tree.symbol] = prefix
    else:
        build_huffman_codes(tree.left, prefix + "0", code_dict)
        build_huffman_codes(tree.right, prefix + "1", code_dict)

    return code_dict

def huffman_encode(input_string, huffman_codes):
    encoded_data = ""
    for char in input_string:
        encoded_data += huffman_codes[char]
    return encoded_data

def huffman_decode(encoded_data, huffman_tree):
    decoded_data = []
    current_node = huffman_tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.symbol is not None:
            decoded_data.append(current_node.symbol)
            current_node = huffman_tree

    return ''.join(decoded_data)

def main():
    input_string = "My name is Aliyan Sajid"
    frequency_dict = Counter(input_string)
    huffman_tree = build_huffman_tree(frequency_dict)
    huffman_codes = build_huffman_codes(huffman_tree)
    encoded_data = huffman_encode(input_string, huffman_codes)
    print(f"String: {input_string}")
    print(f"Encoded Data: {encoded_data}")
    decoded_data = huffman_decode(encoded_data, huffman_tree)
    print(f"Decoded Data: {decoded_data}")

if __name__ == '__main__':
    main()