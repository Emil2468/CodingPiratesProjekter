import random

x = 500
y = 500

xMus = 750
yMus = 500

xMove = 0
yMove = 0
snake = []
objSize = 10

# Ideer:
#   * Lav et tjek for om man støder ind i sig selv. Dette kan gøres med et for-loop og inde i det loop 
#     tjekke om nogle af slanges dele er har samme værdi som den foreste del af slangen. Hvis man støder 
#     ind i sig selv kan spillet sluttes med exit(), eller man kan stoppe med at opdatere ved at kalde noLoop()
#   * Lav slangen i forskellige farver. Eksempelvis kan hovedet have en anden farve, eller hver del af 
#     slangen kan have sin egen farve. Kan laves ved at kalde fill() inde i loopet der tegner slangen, 
#     og give fill forskellige farver at tegne med
#   * Lav ting på banen man ikke må ramme. Dette kan laves ved at kombinere måden musene laves på og måden 
#     jeg foreslår at lave ide 1 på. Man kunne også gøre så slangen bliver kortere hvis man rammer de forbudte 
#     ting, det kan laves med såkaldt "slicing" som laves ved lst[:5] hvilket resulterer i de første 5 elementer 
#     i listen lst

def setup():
    size(1000,1000)
    background(52)
    noStroke()
    frameRate(20)
    snake.append((x,y))
    
def draw():
    global xMus,yMus
    background(52)
    fill(0,255,0)
    moveSnake()
    for a,b in snake:
        rect(a,b,objSize,objSize)
    fill(150)
    rect(xMus,yMus,objSize,objSize)
    if snake[0] == (xMus,yMus):
        nyMus()
        snake.append((0,0))
        print(snake)
    
def nyMus():
    global xMus, yMus
    
    xMus = random.randint(0, int(width/objSize) - 1) * objSize
    yMus = random.randint(0, int(height/objSize) - 1) * objSize

def moveSnake():
    global xMove, yMove
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
    xOld, yOld = snake[0]
    x = xOld + xMove
    y = yOld + yMove
    if y > height:
        y = 0
    if y < 0:
        y = height
    if x > width:
        x = 0
    if x < 0:
        x = width
    snake[0] = (x, y)
    

def keyPressed():
    global xMove, yMove
    if keyCode == 39:
        xMove = objSize
        yMove = 0
    if keyCode == 37:
        xMove = -objSize
        yMove = 0
    if keyCode == 38:
        xMove = 0
        yMove = -objSize
    if keyCode == 40:
        xMove = 0
        yMove = objSize
