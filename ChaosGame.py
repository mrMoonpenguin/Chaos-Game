import turtle, random


def getAvg(P1, P2):
    return (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2


def draw(polygon):
    for vertex in polygon:
        drawPoint(vertex)

    point = (random.randint(-400, 400), random.randint(-400, 400))
    drawPoint(point)

    for i in range(10**4):
        x = random.randint(0, len(polygon) - 1)
        point = getAvg(polygon[x], point)
        drawPoint(point)


def drawPoint(coordinates):
    turtle.setpos(coordinates)
    turtle.dot()


def setup():
    turtle.ht()
    turtle.penup()
    turtle.delay(0.01)


def main():
    setup()

    A = (0, 300)
    B = (-300, -200)
    C = (300, -200)

    polygon = [A, B, C]

    draw(polygon)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
