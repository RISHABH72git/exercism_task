import math
def cipher_text(plain_text):
    normalize = ""
    for i in plain_text:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9':
            normalize+=i.lower()

    normalize_length = len(normalize)
    if normalize_length <= 1:
        return normalize
    rows = int(math.floor(math.sqrt(normalize_length)))
    cols = int(math.ceil(math.sqrt(normalize_length)))

    if rows * cols < normalize_length:
        rows += 1

    normalize_rows = []
    for i in range(0, normalize_length, cols):
        seq = normalize[i:i+cols]
        if len(seq) < cols:
            seq += " " * (cols - len(seq))
        normalize_rows.append(seq)

    print(normalize_rows, rows,cols)
    encoded_columns = []
    for col in range(cols):
        result = ""
        for row in range(rows):
            result += normalize_rows[row][col]

        encoded_columns.append(result)

    print(encoded_columns)
    return " ".join(encoded_columns)
