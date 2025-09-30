class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_phone_number(number)
        self.area_code = self.number[:3]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"

    def clean_phone_number(self, number):
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
            
        result = ""
        for i in number:
            if i in "@:!":
                raise ValueError("punctuations not permitted")
            if i.isalpha():
                raise ValueError("letters not permitted")
                
            if i.isdigit():
                result+=i
                
        print(result)
        if len(result) == 11 and result[0] != "1":
            raise ValueError("11 digits must start with 1")
        elif len(result) == 11 and result[0] == "1":
            result = result[1:]
        elif len(result) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        self.area_code_and_exchang_code(result)
        
        return result
        
    def area_code_and_exchang_code(self, result):
        if result[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif result[0] == "1":
            raise ValueError("area code cannot start with one")
        elif result[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        elif result[3] == "1":
            raise ValueError("exchange code cannot start with one")