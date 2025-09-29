
def count_words(sentence):
    replaced_sentence = sentence.replace(":", " ").replace(",", " ").replace("!", " ").replace(".", " ").replace("_", " ")
    result = {}
    for i in replaced_sentence.split():
        print(i)
        if i.startswith("'") or i.endswith("'"):
            i = i.strip("'")

        i = i.lower().strip()
        if i.isalpha() or i.isdigit() or "'" in i:
            if i in result:
                result[i] +=1
            else:
                result[i] = 1

    return result
