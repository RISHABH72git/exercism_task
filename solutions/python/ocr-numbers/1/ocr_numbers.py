digit_map = {
    "010101111000": 0,
    "000001001000": 1,
    "010011110000": 2,
    "010011011000": 3,
    "000111001000": 4,
    "010110011000": 5,
    "010110111000": 6,
    "010001001000": 7,
    "010111111000": 8,
    "010111011000": 9,
}

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    num_rows = len(input_grid) // 4
    outputs = []

    for row in range(num_rows):
        digits = {}
        # pick 4 lines belonging to this row
        block = input_grid[row*4:(row+1)*4]

        for i in range(4):  
            if len(block[i]) % 3 != 0:
                raise ValueError("Number of input columns is not a multiple of three")
            for j in range(0, len(block[i]), 3):
                if j in digits:
                    digits[j] = digits[j] + block[i][j:j+3]
                else:
                    digits[j] = block[i][j:j+3]

        row_output = ""
        for k, v in sorted(digits.items()):
            if v[5] == '_':
                row_output += "?"
                continue
            result = "".join("1" if v[ch] in ['_', '|'] else "0" for ch in range(len(v)))
            row_output += str(digit_map.get(result, "?"))
        
        outputs.append(row_output)

    return ",".join(outputs)
