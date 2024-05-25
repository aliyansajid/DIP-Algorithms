from PIL import Image
from collections import Counter, defaultdict
import heapq

def read_image(image_path):
    image = Image.open(image_path)
    image = image.convert("L")
    pixel_data = list(image.getdata())
    return pixel_data, image.size

def calculate_frequency(data):
    return Counter(data)

class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def compress_image(data, codebook):
    compressed_data = ''.join(codebook[pixel] for pixel in data)
    return compressed_data

def decompress_image(compressed_data, huffman_tree):
    node = huffman_tree
    decompressed_data = []
    
    for bit in compressed_data:
        node = node.left if bit == "0" else node.right
        if node.left is None and node.right is None:
            decompressed_data.append(node.symbol)
            node = huffman_tree
    
    return decompressed_data

def save_compressed_data(compressed_data, path):
    with open(path, 'w') as file:
        file.write(compressed_data)

def load_compressed_data(path):
    with open(path, 'r') as file:
        return file.read()

def main():
    image_path = r"C:\Users\Aliyan Sajid\Desktop\Codes\house.jpg"
    compressed_path = "compressed_image.txt"
    decompressed_path = "decompressed_image.jpg"
    
    pixel_data, image_size = read_image(image_path)
    frequency = calculate_frequency(pixel_data)
    huffman_tree = build_huffman_tree(frequency)
    codebook = generate_codes(huffman_tree)
    compressed_data = compress_image(pixel_data, codebook)
    save_compressed_data(compressed_data, compressed_path)
    compressed_data = load_compressed_data(compressed_path)
    decompressed_data = decompress_image(compressed_data, huffman_tree)
    decompressed_image = Image.new("L", image_size)
    decompressed_image.putdata(decompressed_data)
    decompressed_image.save(decompressed_path)
    
    print(f"Image compressed and saved to {compressed_path}")
    print(f"Image decompressed and saved to {decompressed_path}")

if __name__ == "__main__":
    main()