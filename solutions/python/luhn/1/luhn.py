class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        if len(self.card_num.strip()) <= 1:
            return False
        double = False
        card_num_list = []
        for i in self.card_num[::-1]:
            if i.isalpha() or i in "-#%$":
                return False
                
            if i.isdigit():
                if double:
                    double_value = int(i) + int(i)
                    print(double_value)
                    if double_value > 9:
                        count = double_value - 9
                    else:
                        count = double_value
                        
                    card_num_list.append(count)
                    double = False
                else:
                    card_num_list.append(int(i))
                    double = True

        print(card_num_list)
        sum = 0
        for i in card_num_list:
            sum += i

        print(sum)
        return (sum % 10) == 0
        
