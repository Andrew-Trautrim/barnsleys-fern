from graphics import *
import random
import time

WIDTH = 800
HEIGHT = 800

DELAY = 0
DRAW_TRIANGLES = False

X_SCALE = 100
Y_SCALE = -50
X_SHIFT = 3/7 * WIDTH
Y_SHIFT = 4/5 * HEIGHT

def main():
    win = GraphWin("Barnsley's Fern", WIDTH, HEIGHT)
    win.setBackground('black')

    if (DRAW_TRIANGLES):
        drawTriangle1(win)
        drawTriangle2(win)
    
    x = 0
    y = 0
    while True:
        try: 
            r = random.random() * 100
            if r < 1:
                (x, y) = f1(x, y)
            elif r < 86:
                (x, y) = f2(x, y)
            elif r < 93:
                (x, y) = f3(x, y)
            else:
                (x, y) = f4(x, y)
            iter = Point(X_SCALE * x + X_SHIFT, Y_SCALE * y + Y_SHIFT)
            iter.setFill('green')
            iter.draw(win)
            time.sleep(DELAY)
        except KeyboardInterrupt:
            break

    win.close()

def f1(x, y):
    return (0, 0.16 * y)

def f2(x, y):
    return (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.60)

def f3(x, y):
    return (0.20 * x + -0.26 * y, 0.23 * x + 0.22 * y + 1.60)

def f4(x, y):
    return (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)

def drawTriangle1(win):
    line1 = Line(Point(X_SCALE * 0 + X_SHIFT, Y_SCALE * 0 + Y_SHIFT), Point(X_SCALE * 2.68 + X_SHIFT, Y_SCALE * 10 + Y_SHIFT))
    line2 = Line(Point(X_SCALE * 2.68 + X_SHIFT, Y_SCALE * 10 + Y_SHIFT), Point(X_SCALE * 2.4125 + X_SHIFT, Y_SCALE * 3.4 + Y_SHIFT))
    line3 = Line(Point(X_SCALE * 2.4125 + X_SHIFT, Y_SCALE * 3.4 + Y_SHIFT), Point(X_SCALE * 0 + X_SHIFT, Y_SCALE * 0 + Y_SHIFT))
    line1.setFill('red')
    line2.setFill('red')
    line3.setFill('red')
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)

def drawTriangle2(win):
    line1 = Line(Point(X_SCALE * 0 + X_SHIFT, Y_SCALE * 1.67 + Y_SHIFT), Point(X_SCALE * -2.05 + X_SHIFT, Y_SCALE * 4.45 + Y_SHIFT))
    line2 = Line(Point(X_SCALE * -2.05 + X_SHIFT, Y_SCALE * 4.45 + Y_SHIFT), Point(X_SCALE * -0.4 + X_SHIFT, Y_SCALE * 2.9 + Y_SHIFT))
    line3 = Line(Point(X_SCALE * -0.4 + X_SHIFT, Y_SCALE * 2.9 + Y_SHIFT), Point(X_SCALE * 0 + X_SHIFT, Y_SCALE * 1.67 + Y_SHIFT))
    line1.setFill('blue')
    line2.setFill('blue')
    line3.setFill('blue')
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)

main()