import turtle

t = turtle.Turtle()


def curve():
    for i in range(200):

        t.forward(1)
        t.right(1)


def rechtek():
    t.home()
    t.clear()
    t.pencolor("purple")
    # primu dreptunghi
    t.up()
    t.backward(100)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.down()
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    # al doilea dreptunghi
    t.up()
    t.backward(37)
    t.right(90)
    t.forward(75)
    t.down()
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    # eliberarea ecranului
    t.up()
    t.forward(200)
    t.down()


def herz():
    t.home()
    t.clear()
    t.pencolor("red")
    # inima
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    # eliberarea ecranului
    t.up()
    t.forward(200)
    t.down()


def hauser():
    t.home()
    t.clear()
    c = t.clone()
    t.pencolor("blue")
    c.pencolor("green")
    # casele
    t.up()
    c.up()
    t.forward(50)
    c.backward(250)
    t.down()
    c.down()
    t.forward(200)
    c.forward(200)
    t.left(90)
    c.left(90)
    t.forward(100)
    c.forward(100)
    t.left(90)
    c.left(90)
    t.forward(200)
    c.forward(200)
    t.left(90)
    c.left(90)
    t.forward(100)
    c.forward(100)
    t.left(180)
    c.left(180)
    t.forward(100)
    c.forward(100)
    # acoperisurile
    t.right(45)
    c.right(45)
    t.forward(142)
    c.forward(142)
    t.right(90)
    c.right(90)
    t.forward(142)
    c.forward(142)
    # usile
    t.up()
    c.up()
    t.right(45)
    c.right(45)
    t.forward(100)
    c.forward(100)
    t.right(90)
    c.right(90)
    t.forward(170)
    c.forward(170)
    t.right(90)
    c.right(90)
    t.down()
    c.down()
    t.forward(40)
    c.forward(40)
    t.right(90)
    c.right(90)
    t.forward(25)
    c.forward(25)
    t.right(90)
    c.right(90)
    t.forward(40)
    c.forward(40)
    t.left(180)
    c.left(180)
    t.forward(40)
    c.forward(40)
    t.right(90)
    c.right(90)
    # geamurile
    t.up()
    c.up()
    t.forward(50)
    c.forward(50)
    t.down()
    c.down()
    for i in range(4):
        t.forward(30)
        c.forward(30)
        t.left(90)
        c.left(90)
    # eliberarea ecranului
    t.up()
    c.up()
    t.right(90)
    c.right(90)
    t.forward(200)
    c.forward(200)
    t.down()
    c.down()


def menu():
    return """
        1 - Rechtek
        2 - Herz
        3 - Hauser
        4 - Exit
    """


def main():

    while True:
        print(menu())

        opt = int(input("opt = "))

        if opt == 1:
            rechtek()

        if opt == 2:
            herz()

        if opt == 3:
            hauser()

        if opt == 4:
            break


main()
