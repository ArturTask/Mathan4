
def begin(a,b,n,m):
    x=[]
    shift_count = 0
    i=0
    copy_a = a  # копия изначальной матрицы a
    copy_b = b  # копия b
    for i in range(n-1): #цикл смещающийся после обнуления столбца
        if(a[i][i]==0): # диагональный элемент равен нулю
            auuu = "\nпоменяли строки местами!"
            shift_count+=1
            for k in range(i,n):  # вначале проверим в столбце
                if(a[k][i]!=0):
                    bowl = a[i]
                    a[i] = a[k]
                    a[k] = bowl
                    bowl = b[i]
                    bowl2 = copy_b[i]
                    b[i] = b[k]
                    copy_b[i] = copy_b[k]
                    b[k] = bowl
                    copy_b[k] = bowl2
                    break
        # диагональный элемент в поряде
        # copy_a = a  # копия изначальной матрицы a
        # copy_b = b  # копия b
        for u in range(i,n-1): #цикл по столбцам
            j=i
            first = a[u + 1][i]
            b[u+1]=b[u+1]-first*b[i]/a[i][i]
            # print(b[u+1])
            while j < m: #цикл по строке
                # print("a{0}{1}".format(str(u + 1), str(j)) + " = " + str(a[u + 1][j]))
                a[u+1][j] = a[u+1][j]- a[i][j]*first/a[i][i]
                j+=1

    for aaa in range(0,n):
        x.append(0)

    x[n-1] = b[n-1]/a[n-1][n-1] # Здесь заполняем X (находим неизвестные)
    for i in range(n-2,-1,-1):
        j=m-1
        x[i]=b[i]
        while j>(i):
            x[i]-=a[i][j]*x[j]
            j-=1
        x[i]=x[i]/a[i][i]
    return x

    # Выведем ответ красиво (x)
    # print("Поздравляю!!! Ваш ответ:")
    # for i in range(0,n):
    #     print(str(x[0][i])+" = "+ str(round(x[1][i],2)),end="    ")


def check_zeroes(n,m,a): # проверим на нулевые столбцы и строки
    for i in range(n):
        row = 0
        for j in range(m):
            if(a[i][j]==0):
                row+=1
        if(row==m):
            print("Вы ввели пустую строку, повторите ввод")
            return False

    for j in range(m):
        column = 0
        for i in range(n):
            if(a[i][j]==0):
                column+=1
        if(column==n):
            print("Вы ввели пустую колонку, повторите ввод")
            return False

    return True


