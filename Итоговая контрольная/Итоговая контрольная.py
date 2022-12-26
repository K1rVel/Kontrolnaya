#Номер билета - №12
def nums():
    ans = []
    while True:
        n = int(input("Введите число:"))
        if n == 0:
            break
        ans.append(n)
    for i in ans:
        print(i)

nums()






