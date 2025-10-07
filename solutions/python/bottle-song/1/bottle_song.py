numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten"
}
def recite(start, take=1):
    second = "And if one green bottle should accidentally fall,"
    result = []
    for i in range(take):
        if i > 0:
            result.append("")
        bottles = "bottles"
        if start == 1:
            bottles = "bottle"
            
        word = numbers[start]
        result.extend([f"{word} green {bottles} hanging on the wall,"] * 2)
        result.append(second)
        if start == 1:
            third = f"There'll be no green bottles hanging on the wall."
        elif start == 2:
            third = f"There'll be {numbers[start-1].lower()} green bottle hanging on the wall."
        else:
            third = f"There'll be {numbers[start-1].lower()} green bottles hanging on the wall."
        result.append(third)
        start -= 1
    return result