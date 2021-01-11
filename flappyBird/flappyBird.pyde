from bird import Bird
b = None

def setup():
    global b
    size(400,400)
    b = Bird(width, height)
    
    
def draw():
    translate(width/2, height/2)
    background(52)
    b.show()
    
