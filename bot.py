from collections import namedtuple

class bot():

    def __init__(self, playerdata):
        playerdata = namedtuple("playerdata",["money", "card1","card2","bet","action"])
    
    