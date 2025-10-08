import random
import string
class Cipher:
    lowercase = string.ascii_lowercase
    
    def __init__(self, key=None):
        self.key = key if key else "".join(random.choices(Cipher.lowercase, k=100))

    def encode(self, text):
        result = []
        if len(self.key) < len(text):
            self.key = self.key * len(text)
        for i, v in enumerate(text):
            total = Cipher.lowercase.index(v) + Cipher.lowercase.index(self.key[i])
            result.append(Cipher.lowercase[total%26])

        return "".join(result)

    def decode(self, text):
        result = []
        if len(self.key) < len(text):
            self.key = self.key * len(text)
        
        for i, v in enumerate(text):
            total = Cipher.lowercase.index(v) - Cipher.lowercase.index(self.key[i])
            result.append(Cipher.lowercase[total%26])

        return "".join(result)
