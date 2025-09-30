import string
import random

class Robot:
    used_names = set()
    def __init__(self):
        self.name = self.random_name()
    def random_name(self):
        upper_alpha = string.ascii_uppercase
        num_digit = string.digits
        while True:
            result = random.choices(upper_alpha, k=2) + random.choices(num_digit, k=3)
            name = "".join(result)
            if name not in Robot.used_names:
                Robot.used_names.add(name)
                return name
        
    def reset(self):
        self.name = self.random_name()