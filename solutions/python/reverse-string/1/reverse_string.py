def reverse(text):
    result = []
    len_text = len(text)-1
    while len_text >= 0:
        result.append(text[len_text])
        len_text -= 1
    return "".join(result)
