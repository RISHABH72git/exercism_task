numbers_word = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
    1000000000000:"trillion"
}
def say(number):
    if number > 9_999_999_999_99 or number < 0:
        raise ValueError("input out of range")
        
    if number in numbers_word:
        if number >= 100:
            result = "one " +numbers_word[number]
        else:
            result = numbers_word[number]
        return result 
        
    keys = list(numbers_word.keys())
    result = ""
    i = 1
    while i < len(keys):
        if keys[i-1] <= number < keys[i]:
            print(f"lowest key:{keys[i-1]}, numbers {number}")
            if number in numbers_word:
                if number < 10:
                    result += "-" +numbers_word[number]
                else:
                    result += " " +numbers_word[number]
                break
                
            div = number // keys[i-1]
            if number > 100:
                if div not in numbers_word:
                    result+=" " + say(div) + " "+ numbers_word[keys[i-1]]
                else:
                    result+=" " +numbers_word[div] + " "+ numbers_word[keys[i-1]]
            else:
                result+=" "+ numbers_word[keys[i-1]]
            
            number = number % keys[i-1]
            i = 1
        
        i+=1
            
    return result.strip()
