class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[len(self.scores)-1]
    
    def personal_best(self):
        max = self.scores[0]
        for i in self.scores:
            if max < i:
                max = i
        return max
        
    def personal_top_three(self):
        temp_scores = self.scores.copy()
        result = []
        for i in range(min(3,len(temp_scores))):
            first_max = temp_scores[0]
            for j in temp_scores:
                if first_max < j:
                    first_max = j
            result.append(first_max)
            temp_scores.remove(first_max)
                
        return result