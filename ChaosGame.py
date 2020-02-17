import turtle, random

A = (0, 300)
B = (-300, -200)
C = (300, -200)

polygon = [A, B, C]


def getAvg(P1, P2):
    return (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2


def draw():
    start = (random.randint(-400, 400), random.randint(-400, 400))
    drawPoint(start)
    current = start

    for i in range(10**4):
        x = random.randint(0, len(polygon) - 1)
        current = getAvg(polygon[x], current)
        drawPoint(current)


def drawPoint(coordinates):
    turtle.setpos(coordinates)
    turtle.dot()


def setup():
    turtle.ht()
    turtle.penup()
    turtle.delay(0.01)

    for vertex in polygon:
        drawPoint(vertex)


def main():
    setup()
    draw()

    turtle.exitonclick()


if __name__ == '__main__':
    main()
