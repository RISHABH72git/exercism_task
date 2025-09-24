import string
alpha = string.ascii_lowercase
def encode(plain_text):
    encoded = ""
    space = 0
    for i in plain_text.lower():
        if i != " " and i != ',' and i != '.':
            if space > 4:
                encoded += " "
                space = 0
            if i.isdigit():
                encoded += i
            else:
                alpha_index = alpha.index(i)
                encoded +=alpha[-(alpha_index +1)]
            space += 1

    return encoded


def decode(ciphered_text):
    decoded = ""
    for i in ciphered_text:
        if i != " ":
            if i.isdigit():
                decoded += i
            else:
                alpha_index = alpha.index(i)
                decoded += alpha[26-(alpha_index +1)]
    return decoded
        