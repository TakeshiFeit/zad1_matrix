import random

def output(out):
    for i in range(len(out)):
        print (out[i])
    print(" ")

def Choice():
    choice = int(input())
    return choice

def filling(n, matrix):
    print ("select filling method")
    print ("1 = random, 2 = from file")
    choice = Choice()

    if choice == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] = random.randrange(-10, 10)
        return matrix

    elif choice == 2:
        file = open("text.txt", "r")
        for i in range(n):
            symbol = file.readline().split()
            for j in range(n):
                matrix[i][j]=int(symbol[j])
        return matrix

    else:
        print("error")

def condition(matrix):
    s2 = 0
    s4 = 0
    count = 1
    point = len(matrix) // 2 + 1
    while count != point:

        for j in range(count,n-count):
            if (j%2==0) and ((matrix[count-1][j])==0):
                s2 = count
            if (count%2==0) and ((matrix[n-count][j])>=0):
                s4 += matrix[n-count][j]
        count+=1

    return s2, s4

def change(matrix, s2, s4):

    count = 1
    point = len(matrix) // 2 + 1
    if s2>s4:
        while count != point:
            for q in range(count,n-count):
                y = matrix[count-1][q]
                matrix[count-1][q] = matrix[q][count-1]
                matrix[q][count-1] = y
                del y
            count += 1
    else: 
        while count != point:
            for q in range(count,n-count):
                y = matrix[count-1][q]
                matrix[count-1][q] = matrix[q][n-count]
                matrix[q][n-count] = y
                del y
            count += 1

    return matrix

def multMatMat(n, mat1, mat2):
    result = []
    for i in range(n):
        result.append([0] * n)
    for i in range(n):
        for j in range(n):
            result[i][j] = (mat1[i][j] * mat2[j][i]) 
    return result

def multNumMat(n, num, mat):
    result = []
    for i in range(n):
        result.append([0] * n)
    for i in range(n):
        for j in range(n):
            result[i][j] = (mat[i][j] * num) 
    return result

def minus(n, mat1,mat2):
    result = []
    for i in range(n):
        result.append([0] * n)
    for i in range(n):
        for j in range(n):
            result[i][j]=(mat1[i][j]-mat2[i][j]) 
    return result

print ("enter N ")
n = int(input())
print ("enter K ")
k = int(input())

matrixA = []
matrixF = []
matrixAt = []
for i in range(n):
        matrixA.append([0] * n)
        matrixF.append([0] * n)
        matrixAt.append([0] * n)

filling(n, matrixA)

print("matrixA:")
output(matrixA)

for i in range(n):
    for j in range(n):
        matrixF[i][j] = matrixA[i][j]
        matrixAt[i][j] = matrixA[j][i]

s2,s4 = condition(matrixF)
change(matrixF, s2, s4)
print("matrixF:")
output(matrixF)

print("matrixAt:")
output(matrixAt)

result1 = multNumMat(n, k, matrixF)
result1 = multMatMat(n, result1, matrixA)
result2 = multNumMat(n, k, matrixAt)

print("result:")
output(minus(n, result1, result2))

