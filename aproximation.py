import matplotlib.pyplot as plt
import math
import Gauss



def draw(x_y,count_y,name):
    min = 1000000
    max = -1000000
    for i in range(0,len(x_y)):
        x = x_y[i][0]
        if(min > x):
            min = x
        if (max < x):
            max = x

    fig = plt.figure()
    axes = fig.add_subplot(111)
    for i in range(0, len(x_y)):
        x = x_y[i][0]
        y = x_y[i][1]
        axes.scatter(x, y)
    axes.grid()
    a = []
    b = []
    for i in range(int(min)*10,int(max+1)*10):
        x = i / 10
        a.append(x)
        b.append(count_y(x))
    axes.plot(a,b)
    plt.title(name)
    plt.show()




def linear_aproxomation(x_y):

    sx = 0
    sy = sx
    sxx = sx
    sxy = sx
    for i in range(0,len(x_y)):
        sx = sx + x_y[i][0]
        sy= sy + x_y[i][1]
        sxx = sxx + x_y[i][0] * x_y[i][0]
        sxy = sxy + x_y[i][0] * x_y[i][1]
    # подготовка данных для метода Гаусса
    a=[]
    b=[]
    n=2
    m=n
    temp =[sxx,sx]
    a.append(temp)
    temp = [sx,len(x_y)]
    a.append(temp)
    b.append(sxy)
    b.append(sy)
    # подготовка данных для метода Гаусса
    answer = Gauss.begin(a,b,n,m)

    # коэф Пиросона:
    mid_x = sx / len(x_y)
    mid_y = sy / len(x_y)
    sxy = 0
    sx = 0
    sy = 0
    for i in range(0,len(x_y)):
        sxy = sxy + (x_y[i][0] - mid_x)*(x_y[i][1] - mid_y)
        sx = sx + (x_y[i][0] - mid_x)*(x_y[i][0] - mid_x)
        sy = sy + (x_y[i][1] - mid_y)*(x_y[i][1] - mid_y)

    answer.append(sxy/math.sqrt(sx*sy)) # вставляем коэф Пирсона

    def count_y(x):
        return answer[0]*x + answer[1]

    S=0
    for i in range(0,len(x_y)):
        x = x_y[i][0]
        y = x_y[i][1]
        S = S + (count_y(x)-y)*(count_y(x)-y)


    answer.append(float(S))

    draw(x_y,count_y,"Линейная ф-я")

    return answer

def polynom_aproximation(x_y):
    sx = 0
    sxx = 0
    sxxx = 0
    sxxxx = 0
    sy = 0
    sxy = 0
    sxxy = 0
    for i in range(0, len(x_y)):
        sx = sx + x_y[i][0]
        sxx = sxx + x_y[i][0] * x_y[i][0]
        sxxx = sxxx + x_y[i][0] * x_y[i][0] * x_y[i][0]
        sxxxx = sxxxx + x_y[i][0] * x_y[i][0] * x_y[i][0] * x_y[i][0]
        sy = sy + x_y[i][1]
        sxy = sxy + x_y[i][0] * x_y[i][1]
        sxxy = sxxy + x_y[i][0] * x_y[i][0] * x_y[i][1]

    a = []
    b = []
    n = 3
    m = n
    temp = [len(x_y),sx,sxx]
    a.append(temp)
    temp = [sx, sxx, sxxx]
    a.append(temp)
    temp = [sxx, sxxx, sxxxx]
    a.append(temp)

    b.append(sy)
    b.append(sxy)
    b.append(sxxy)

    answer = Gauss.begin(a, b, n, m)

    def count_y(x):
        return answer[2]*x*x + answer[1]*x + answer[0]

    S=0
    for i in range(0,len(x_y)):
        x = x_y[i][0]
        y = x_y[i][1]
        S = S + (count_y(x)-y)*(count_y(x)-y)

    answer.append(float(S))

    draw(x_y, count_y, "Полиномиальная(2 степени) ф-я")

    return answer


def exp_aproximation(x_y):
    sx = 0
    sxx = 0
    slny = 0
    sxlny = 0

    for i in range(0, len(x_y)):
        sx = sx + x_y[i][0]
        sxx = sxx + x_y[i][0] * x_y[i][0]
        slny = slny + math.log(x_y[i][1]) # здесь логарифм => х>0
        sxlny = sxlny + x_y[i][0] * math.log(x_y[i][1])

    n = len(x_y)
    b = (n*sxlny - sx*slny)/(n*sxx - sx*sx)
    a = slny/n - sx*b/n
    answer=[]
    answer.append(a)
    answer.append(b)

    def count_y(x):
        return math.exp(answer[0] + answer[1]*x)

    S=0
    for i in range(0,len(x_y)):
        x = x_y[i][0]
        y = x_y[i][1]
        S = S + (count_y(x)-y)*(count_y(x)-y)

    answer.append(float(S))

    draw(x_y, count_y, "Экспоненциальная ф-я")

    return answer

def log_aproximation(x_y):
    slnx = 0
    slnxlnx = 0
    sy = 0
    sylnx = 0

    for i in range(0, len(x_y)):
        sy = sy + x_y[i][1]
        sylnx = sylnx + x_y[i][1] * math.log(x_y[i][0])
        slnx = slnx + math.log(x_y[i][0])
        slnxlnx = slnxlnx + math.log(x_y[i][0]) * math.log(x_y[i][0])

    n = len(x_y)
    b = (n*sylnx - slnx*sy)/(n*slnxlnx - slnx*slnx)
    a = sy/n - slnx*b/n
    answer = []
    answer.append(a)
    answer.append(b)

    def count_y(x):
        return answer[0] + answer[1]*math.log(x)

    S=0
    for i in range(0,len(x_y)):
        x = x_y[i][0]
        y = x_y[i][1]
        S = S + (count_y(x)-y)*(count_y(x)-y)

    answer.append(float(S))

    draw(x_y, count_y, "Логарифмическая ф-я")

    return answer

def pow_aproximation(x_y):
    slnx = 0
    slny = 0
    slnxlny = 0
    slnxlnx = 0
    for i in range(0, len(x_y)):
        slnx = slnx + math.log(x_y[i][0])
        slny = slny + math.log(x_y[i][1])
        slnxlnx = slnxlnx + math.log(x_y[i][0])*math.log(x_y[i][0])
        slnxlny = slnxlny + math.log(x_y[i][0]) * math.log(x_y[i][1])

    n = len(x_y)
    b = (n*slnxlny - slnx*slny)/(n*slnxlnx - slnx*slnx)
    a = math.exp(slny/n - slnx*b/n)
    answer = []
    answer.append(a)
    answer.append(b)

    def count_y(x):
        return answer[0] * math.pow(x,answer[1])

    S = 0
    for i in range(0, len(x_y)):
        x = x_y[i][0]
        y = x_y[i][1]
        S = S + (count_y(x) - y) * (count_y(x) - y)

    answer.append(float(S))

    draw(x_y, count_y, "Степенная ф-я")

    return answer


