from graphics import *
import time, random 

point1 = (100, 100)

point2 = (150, 50)

def retrieveData():
    
    data_file = open('data.txt', 'r')

    dataList = data_file.read().split('\n')

    data_file.close()


    
    r = random.choice(data_file)

    red = random.choice(data_file)

    green = random.choice(data_file)

    blue = random.choice(data_file)





def bounceInWind(shape, dx, dy, xLow, xHigh, yLow, yHigh):

    delay = .50
    for i in range(500):
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()

        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx 
        if y < yLow:
            dy = -dy
        elif y > yHigh:
            dy = -dy

    time.sleep(delay)
    

def makeBall(center, radius, graph):
    ball = Circle(center, radius)
    ball.setFill(color_rgb(10, 60, 80))
    ball.setOutline(color_rgb(10, 10, 10))
    ball.draw(graph)
    return ball

    
def getRandPoint(xLow, xHigh, yLow, yHigh):
    x = random.randrange(xLow, xHigh+2)
    y = random.randrange(yLow, yHigh+2)
    return Point(x,y)

    
def changeSize(radius):
        center = getCenter()
        
        if radius < xLow:
            data_file
            radius = r
                
        elif radius > xHigh:
            data_file
            radius = r
        if radius < yLow:
            data_file
            radius = r
            
        elif radius > yHigh:
            data_file
            radius = r
            
    
def changeColour(Red, Green, Blue):
    
        center = getCenter()
    
        if radius < xLow:
            retrieveData()
            Red = red
            Green = green
            Blue = blue
        
        if radius > xHigh:
            retrieveData()
            Red = red
            Green = green
            Blue = blue
        
        if radius < yLow:
            retrieveData()
            Red = red
            Green = green
            Blue = blue
        
        if radius > yHigh:
            retrieveData()
            Red = red
            Green = green
            Blue = blue
        
        
        
def pingBall(dx, dy):
    graphWidth = 400
    graphHeight = 400
    graph = GraphWin('boxbounce', graphWidth, graphHeight)
    graph.setCoords(0, 0, graphWidth, graphHeight)
    
    radius = 20
    xLow = radius
    xHeight = graphWidth - radius
    yLow = radius 
    yHeight = graphHeight - radius 

    center = getRandPoint(xLow, xHeight, yLow, yHeight)
    ball = makeBall(point1, point2, graph)

    bounceInWind(ball, dx, dy, xLow, xHeight, yLow, yHeight)
                 
    changeSize(radius)
                 
    changeColour(color_rgb("Red", "Green", "Blue"))
    

    graph.close

                 
pingBall(6, 8)












