nTriangles = 10

def setup():
    size(1000,1000)
    noStroke()
    for i in range(nTriangles):
        yOffset = i * 50
        xOffset = 100 + i * 20
        xStart = 500
        ballSize = 20
        fill(0,50,0)
        triangle(xStart, 200 + yOffset, 
                 xStart - xOffset, 300 + yOffset,
                 xStart + xOffset, 300 + yOffset)
        fill(200,0,0)
        # ellipse(xStart - xOffset, 300 + yOffset,ballSize,ballSize)
        # ellipse(xStart + xOffset, 300 + yOffset,ballSize,ballSize)
