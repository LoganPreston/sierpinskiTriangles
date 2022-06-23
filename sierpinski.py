import argparse
import random
import matplotlib.pyplot as plt
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numPts', type=int,\
            help='how many points do you want')
    parser.add_argument('--showTime', action='store_true',\
            help='show the time it takes to perform steps')
    args = parser.parse_args()
    numPts = args.numPts
    showTime = args.showTime

    #border points are key for randidx
    points = [(0,0),(7.5,13),(15,0)]
    lenPoints = len(points)
    
    #init one non-randomly
    x = (points[0][0] + points[1][0]) / 2
    y = (points[0][1] + points[1][1]) / 2
    lastPt = (x,y)
    points.append(lastPt)

    start = time.time()
    for i in range(numPts):
        randIdx = random.randint(0,2)
        randBorderPt = points[randIdx]
 
        x = (lastPt[0] + randBorderPt[0]) / 2
        y = (lastPt[1] + randBorderPt[1]) / 2

        lastPt = (x,y)
        points.append(lastPt)
        lenPoints += 1

    if(showTime):
        print("time to get pts: ", time.time() - start)
    
    start = time.time()
    listXVals = list(zip(*points))[0]
    listYVals = list(zip(*points))[1]
    maxXVal = max(listXVals)
    maxYVal = max(listYVals)
    
    xColors = [color / maxXVal for color in listXVals]
    yColors = [color / maxYVal for color in listYVals]
    zeroColors = [max(0,1-xColor-yColor) for xColor,yColor in zip(xColors, yColors)] 
    colors = list(zip(yColors, zeroColors, xColors))
    plt.scatter(*zip(*points), s = 1, c = colors)
    if(showTime):
        print("time to plot: ", time.time() - start)
    
    plt.show()

if __name__ == '__main__':
    main()
