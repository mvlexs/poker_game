import random

class Card():
    colors = ["Club","Spade","Diamond","Heart"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self, value, color):
        self.value = ""
        self.color = ""

    def get_color(self, colors):
        self.color = random.choice(colors)
        return self.color
        
    def get_value(self, values):
        self.value = random.choice(values)
        return self.value
    
    def __repr__(self) -> str:
        rep = "[" + self.color + " " + self.value + "]"
        return rep
