import string
def abbreviate(words):
    capital_alpha = string.ascii_uppercase
    custom_words = words.replace("-", " ").split(" ")
    result = ""
    for i in custom_words:
        j = 0
        while j < len(i):
            if i[j].isalpha():
                result += i[j].upper()
                break
            j += 1
    return result
