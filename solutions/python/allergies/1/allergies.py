class Allergies:
    Item = {
         128: "cats",
         64: "pollen",
         32: "chocolate",
         16: "tomatoes",
         8: "strawberries",
         4: "shellfish",
         2: "peanuts",
         1: "eggs"
        }
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if self.score in Allergies.Item:
            return Allergies.Item[self.score] == item

        temp_score = self.score
        result = []
        for key in Allergies.Item:
            if temp_score - key > 0:
                temp_score = temp_score - key
                result.append(Allergies.Item[key])
                if temp_score in Allergies.Item:
                    result.append(Allergies.Item[temp_score])
                    break

        return item in result

    @property
    def lst(self):
        if self.score in Allergies.Item:
            return [Allergies.Item[self.score]]

        result = []
        temp_score = self.score
        if self.score > 255:
            n = 128
            while n < self.score:
                if n*2 < self.score:
                    n = n*2
                else:
                    break
            temp_score = self.score % n
        
        
        for key in Allergies.Item:
            if temp_score - key >= 0:
                temp_score = temp_score - key
                result.append(Allergies.Item[key])
                if temp_score in Allergies.Item:
                    result.append(Allergies.Item[temp_score])
                    break
        print(result)
        return result
