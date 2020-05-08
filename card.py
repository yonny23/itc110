class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
        self.value=0
       
        
    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getValue(self):
        if self.rank > 10:
            self.value=10
        else:
            self.value=self.rank
        return self.value

    def setSuit(self):
        self.su=""
        if self.suit =="d":
            self.su="diamonds"
        elif self.suit=="h":
            self.su="hearts"
        elif self.suit=="s":
            self.su="spades"
        else:
            self.su ="clubs"
        return self.su

    
    
    def __str__(self):
        
        if self.rank >1 and self.rank< 11:
            self.name=str(self.rank) + " of " + self.setSuit()
        if self.rank==1:
            self.name="the ace of " + self.setSuit()
        if self.rank==11:
            self.name="the jack of " + self.setSuit()
        if self.rank==12:
             self.name="the queen of " + self.setSuit()
        if self.rank==13:
             self.name="the king of " + self.setSuit()
        return self.name

def main():
    card=Card(9,"s")
    print(card)

main()
