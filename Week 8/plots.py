import matplotlib.pyplot as plt
from dateutil.tz.win import valuestodict


# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# plt.plot(x,y)
# plt.show()

# def small():
#     x = [3, 3, 4, 4, 3]
#     y = [3, 4, 4, 3, 3]
#     plt.plot(x,y,'ro--')
#
# def medium():
#     x = [2, 2, 5, 5, 2]
#     y = [2, 5, 5, 2, 2]
#     plt.plot(x,y,'gs--')
#
# def large():
#     x = [1, 1, 6, 6, 1]
#     y = [1, 6, 6, 1, 1]
#     plt.plot(x,y,'b-p')
#
# small()
# medium()
# large()
#
# plt.show()

def coordinate():
    print("Enter a X value")
    x= int(input())
    print("Enter a Y value")
    y= int(input())
    return x, y


def path():
    print("Retrieving path")
    x_values = []
    y_values = []
    for i in range(4):
        data= coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values,y_values ]

def run_task3():
    values= path()
    x= values[0]
    y= values[1]

    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.plot(x,y,'ro--')
    plt.show()
run_task3()

