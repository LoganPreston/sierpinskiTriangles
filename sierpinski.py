import argparse
import random
import matplotlib.pyplot as plt
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numPts', type=int,\
            help='how many points do you want')
    parser.add_argument('--showTime', type=bool,\
            help='show the time it takes to perform steps')
    args = parser.parse_args()
    numPts = args.numPts
    showTime = args.showTime

    #start with border points
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
        randPt = points[randIdx]
 
        x = (lastPt[0] + randPt[0]) / 2
        y = (lastPt[1] + randPt[1]) / 2

        lastPt = (x,y)
        points.append(lastPt)
        lenPoints += 1

    if(showTime):
        print("time to get pts: ", time.time() - start)
    start = time.time()
    plt.scatter(*zip(*points), s = 1, c = 'blue')
    if(showTime):
        print("time to plot: ", time.time() - start)
    plt.show()

if __name__ == '__main__':
    main()
