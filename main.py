import math
import inputDots
import aproximation
import outputDots
import sys
# e = sys.exc_info()[1]
#print(e.args[0])
f = open("out.txt","w")

S = [] # массив для мер отклонений
delta = [] # массив среднеквадратичных отклонений

x_y = inputDots.input_x_y()
print("Вывести в файл? нет - 0 да - 1")
output_mode = int(input())

outputDots.my_print(f,output_mode,"Линейная апроксимация функции:")
try:
    x = aproximation.linear_aproxomation(x_y)
    outputDots.my_print(f,output_mode,f"φ = {x[0]:.3f}x + ({x[1]:.3f})")
    outputDots.my_print(f,output_mode,f"коэффициент Пирсона r = {x[2]}")
    outputDots.my_print(f,output_mode,f"S = {x[3]}")
    delta.append(math.sqrt(x[3]/len(x_y)))
    outputDots.my_print(f,output_mode,f"δ = {delta[0]}\n")
    S.append(x[3])

except Exception:
    outputDots.my_print(f,output_mode,"при подсчете апроксимирующей функции произошла недопустимая операция(деление на ноль или логарифм от неположительного числа)")


outputDots.my_print(f,output_mode,"Полиномиальная(2 степени) апроксимации функции:")
try:
    x = aproximation.polynom_aproximation(x_y)
    outputDots.my_print(f,output_mode,f"φ = {x[2]:.3f}x^2 + ({x[1]:.3f}x) + ({x[0]:.3f})")
    outputDots.my_print(f,output_mode,f"S = {x[3]}")
    delta.append(math.sqrt(x[3] / len(x_y)))
    outputDots.my_print(f,output_mode,f"δ = {delta[1]}\n")
    S.append(x[3])
except Exception:
    outputDots.my_print(f,output_mode,"при подсчете апроксимирующей функции произошла недопустимая операция(деление на ноль или логарифм от неположительного числа)")


outputDots.my_print(f,output_mode,"Экспоненциальная апроксимации функции:")
try:
    x = aproximation.exp_aproximation(x_y)
    outputDots.my_print(f,output_mode,f"φ = exp({x[0]:.3f} + {x[1]:.3f}x )")
    outputDots.my_print(f,output_mode,f"S = {x[2]}")
    delta.append(math.sqrt(x[2] / len(x_y)))
    outputDots.my_print(f,output_mode,f"δ = {delta[2]}\n")
    S.append(x[2])
except Exception:
    outputDots.my_print(f,output_mode,"при подсчете апроксимирующей функции произошла недопустимая операция(деление на ноль или логарифм от неположительного числа)")

outputDots.my_print(f,output_mode,"Логарифмическая апроксимации функции:")
try:
    x = aproximation.log_aproximation(x_y)
    outputDots.my_print(f,output_mode,f"φ = {x[0]:.3f} + {x[1]:.3f}ln(x)")
    outputDots.my_print(f,output_mode,f"S = {x[2]}")
    delta.append(math.sqrt(x[2] / len(x_y)))
    outputDots.my_print(f,output_mode,f"δ = {delta[3]}\n")
    S.append(x[2])
except Exception:
    outputDots.my_print(f,output_mode,"при подсчете апроксимирующей функции произошла недопустимая операция(деление на ноль или логарифм от неположительного числа)")

outputDots.my_print(f,output_mode,"Степенная апроксимации функции:")
try:
    x = aproximation.pow_aproximation(x_y)
    outputDots.my_print(f,output_mode,f"φ = {x[0]:.3f}*x^({x[1]:.3f})")
    outputDots.my_print(f,output_mode,f"S = {x[2]}")
    delta.append(math.sqrt(x[2] / len(x_y)))
    outputDots.my_print(f,output_mode,f"δ = {delta[4]}\n")
    S.append(x[2])
except Exception:
    outputDots.my_print(f,output_mode,"при подсчете апроксимирующей функции произошла недопустимая операция(деление на ноль или логарифм от неположительного числа)")

number_of_min = 0
min = 100000.0
for i in range(0,len(delta)):
    if(min > delta[i]):
        min = delta[i]
        number_of_min = i


if(number_of_min==0):
    outputDots.my_print(f,output_mode,f"Наилучшая апроксимирующая функция - Линейная, δ = {delta[number_of_min]}")
elif(number_of_min==1):
    outputDots.my_print(f,output_mode,f"Наилучшая апроксимирующая функция - Полиномиальная(2 степени), δ = {delta[number_of_min]}")
elif (number_of_min == 2):
    outputDots.my_print(f,output_mode,f"Наилучшая апроксимирующая функция - Экспоненциальная, δ = {delta[number_of_min]}")
elif (number_of_min == 3):
    outputDots.my_print(f,output_mode,f"Наилучшая апроксимирующая функция - Логарифмическая, δ = {delta[number_of_min]}")
elif (number_of_min == 4):
    outputDots.my_print(f,output_mode,f"Наилучшая апроксимирующая функция - Степенная, δ = {delta[number_of_min]}")

f.close()

# 1 2.7
# 2 7.29
# 3 19.68
# 4 53.144
# 5 143.49
# 6 387.42
# 7 400
# 8 500
# 9 650
# 10 770
# 11 890
# 12 1000


