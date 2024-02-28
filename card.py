import random

class Card():

  
    colors = ["Club","Spade","Diamond","Heart"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]  
    color = "a"
    value = "b"
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def set_color(self, color_counter):
        
        next_color = Card.colors[color_counter%4]
        
        return next_color

        
    def set_value(self, value_counter, color_counter):

       
        next_value = Card.values[value_counter%13]

        if next_value == "A":
                color_counter += 1
        else:
                pass


        
        return next_value, color_counter
        
    
    def get_color(self):
        return self.color
    
    def get_value(self):
        return self.value
    
    def __repr__(self) -> str:
        rep = f'[{self.get_value()} {self.get_color()}]'
        return rep
