from matplotlib import pyplot as plt
from math import sqrt

print("Start Entering the sequence of Commands")
print("Command 1 : ({Distance}, {Direction})")
print("Command 2 : Interpret")
print("Command 3 : Plot")
print("Once you are done press Enter")

x = []
y = []

x.append(0)
y.append(0)

def interpret():
    final_x = x[len(x) - 1]
    final_y = y[len(y) - 1]

    displacement = sqrt(final_x**2 + final_y**2)

    if final_x == 0 and final_y == 0:
        print("You are back to starting pos")
    elif final_x == 0:
        if final_y > 0:
            print(f"{displacement} N")
        else:
            print(f"{displacement} S")
    elif final_y == 0:
        if final_x > 0:
            print(f"{displacement} E")
        else:
            print(f"{displacement} W")
    else:
        if final_x > 0 and final_y > 0:
            print(f"{displacement} NE")
        elif final_x < 0 and final_y > 0:
            print(f"{displacement} NW")
        elif final_x > 0 and final_y < 0:
            print(f"{displacement} SE")
        elif final_x < 0 and final_y < 0:
            print(f"{displacement} SW")


def plot():
    plt.plot(x, y, marker="o")
    plt.show()

while True:
    s = input()

    if not s:
        break

    if s == "Interpret":
        interpret()
        continue

    if s == "Plot":
        plot()
        continue

    
    r, w = map(str, s.split(","))
    r = r.strip()
    w = w.strip()

    r = float(r)

    x_last = x[len(x) - 1]
    y_last = y[len(y) - 1]

    x_new = -1
    y_new = -1

    if w == "N":
        x_new = x_last
        y_new = y_last + r

    if w == "S":
        x_new = x_last
        y_new = y_last - r

    if w == "E":
        x_new = x_last + r
        y_new = y_last

    if w == "W":
        x_new = x_last - r
        y_new = y_last

    r = r / sqrt(2)

    if w == "NW":
        x_new = x_last - r
        y_new = y_last + r

    if w == "NE":
        x_new = x_last + r
        y_new = y_last + r

    if w == "SW":
        x_new = x_last - r
        y_new = y_last - r
    if w == "SE":
        x_new = x_last + r
        y_new = y_last - r

    x.append(x_new)
    y.append(y_new)


