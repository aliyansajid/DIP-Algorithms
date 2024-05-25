class ShannonFanoNode:
    def __init__(self, symbol=None, probability=0.0):
        self.symbol = symbol
        self.probability = probability
        self.code = ""
        self.left = None
        self.right = None

def shannon_fano(nodes):
    if len(nodes) == 1:
        return
    nodes.sort(key=lambda x: x.probability, reverse=True)
    total = sum(node.probability for node in nodes)
    cumulative = 0
    for i, node in enumerate(nodes):
        cumulative += node.probability
        if cumulative >= total / 2:
            break
    left = nodes[:i + 1]
    right = nodes[i + 1:]
    for node in left:
        node.code += "0"
    for node in right:
        node.code += "1"
    shannon_fano(left)
    shannon_fano(right)

def get_codes(nodes):
    codes = {}
    for node in nodes:
        codes[node.symbol] = node.code
    return codes

def shannon_fano_encoding(data):
    frequencies = {}
    for symbol in data:
        if symbol in frequencies:
            frequencies[symbol] += 1
        else:
            frequencies[symbol] = 1
    
    total_symbols = len(data)
    nodes = [ShannonFanoNode(symbol, frequency / total_symbols) for symbol, frequency in frequencies.items()]

    shannon_fano(nodes)
    codes = get_codes(nodes)

    encoded_data = "".join(codes[symbol] for symbol in data)

    return codes, encoded_data

data = "abracadabra"
codes, encoded_data = shannon_fano_encoding(data)
print("Codes:", codes)
print("Encoded Data:", encoded_data)