class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return "{name} {score}".format(**self)
        
    def comparator(a, b):
        # compare by score, if score is equal sort by alphabet
        if a.score == b.score:
            if a.name < b.name:
                return -1
            if a.name == b.name:
                return 0
            return 1
        
        return -1 if a.score > b.score else 1

        

