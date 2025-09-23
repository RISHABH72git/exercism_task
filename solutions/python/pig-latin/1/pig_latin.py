def pig_latin(text):
    vowels = ("a", "e", "i", "o", "u")
    word = text
    if word.startswith(vowels) or word.startswith(("xr", "yt")):
        return word + "ay"

    i = 0
    while i < len(word):
        # Rule 3: consonant(s) + "qu"
        if word[i:i+2] == "qu":
            i += 2
            continue
        # Rule 2 or 4: first vowel or 'y' acting as vowel
        if word[i] in vowels or (word[i] == "y" and i != 0):
            break
        i += 1

    return word[i:] + word[:i] + "ay"


def translate(sentence: str) -> str:
    return " ".join(pig_latin(word) for word in sentence.split())

