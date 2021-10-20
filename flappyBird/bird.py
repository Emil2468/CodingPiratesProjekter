class Bird():
    def __init__(self, width, height):
        self.score = 0
        self.pos = PVector(-width/4, 0)
        
    def show(self):
        fill(0,255,255)
        rect(self.pos.x, self.pos.y,10,50)
