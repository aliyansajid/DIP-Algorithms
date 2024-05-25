class LZ77:
    def __init__(self, window_size=20, lookahead_buffer_size=15):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, data):
        i = 0
        output = []

        while i < len(data):
            match = self.find_longest_match(data, i)

            if match:
                (best_match_distance, best_match_length) = match
                output.append((best_match_distance, best_match_length, data[i + best_match_length]))
                i += best_match_length + 1
            else:
                output.append((0, 0, data[i]))
                i += 1

        return output

    def find_longest_match(self, data, current_position):
        end_of_buffer = min(current_position + self.lookahead_buffer_size, len(data))

        best_match_distance = -1
        best_match_length = -1

        for j in range(current_position + 1, end_of_buffer):
            start_index = max(0, current_position - self.window_size)
            substring = data[current_position:j]

            for k in range(start_index, current_position):
                repeat_length = 0

                while repeat_length < j - current_position and data[k + repeat_length] == data[current_position + repeat_length]:
                    repeat_length += 1

                if repeat_length > best_match_length:
                    best_match_distance = current_position - k
                    best_match_length = repeat_length

        if best_match_distance > 0 and best_match_length > 0:
            return best_match_distance, best_match_length
        return None

data = "abracadabra"
lz77 = LZ77(window_size=6, lookahead_buffer_size=4)
compressed_data = lz77.compress(data)
print(compressed_data)