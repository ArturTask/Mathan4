import numpy as np
import matplotlib.pyplot as plt
import math


def input_x_y():
    x_y=[]
    print("Ввсети точки вручную - 0 из файла - 1")
    input_mode = int(input())

    if(input_mode==0):
        print("Введите количество точек")
        n = int(input())
        print("Вводите точки в формате: X Y, 2 значения через пробел, где X - абсцисса Y - орлината точки")
        for i in range(0,n):
            temp = input().split()
            temp[0]=float(temp[0])
            temp[1] = float(temp[1])
            x_y.append(temp)
    elif(input_mode==1):
        try:
            f = open("in.txt", "r")  # решил без ввода пути
            words = []
            for line in f:  # считываю построчно и кладу в список
                words.append(line)
            n = int(words[0])
            for i in range(1, n+1):
                temp = words[i].split()
                temp[0] = float(temp[0])
                temp[1] = float(temp[1])
                x_y.append(temp)
        finally:
            f.close()

    # print(x_y)

    fig = plt.figure()
    axes = fig.add_subplot(111)
    for i in range(0,n):
        x=x_y[i][0]
        y=x_y[i][1]
        axes.scatter(x,y)
    axes.grid()
    plt.title("Ваши точки")
    plt.show()

    return x_y





