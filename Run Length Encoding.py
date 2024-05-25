def run_length_encoding(input_string):
    if not input_string:
        return ""

    encoded_string = ""
    count = 1
    previous_char = input_string[0]

    for char in input_string[1:]:
        if char == previous_char:
            count += 1
        else:
            encoded_string += previous_char + str(count)
            previous_char = char
            count = 1

    encoded_string += previous_char + str(count)
    return encoded_string

input_string = "aaabbccccd"
encoded_string = run_length_encoding(input_string)
print(f"Original string: {input_string}")
print(f"Encoded string: {encoded_string}")