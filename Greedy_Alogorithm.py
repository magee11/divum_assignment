def Fgreedy(cash):
    posibility = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    n = len(posibility)
    final = []
    i = n - 1
    while i >= 0:
        while cash >= posibility[i]:
            cash = cash - posibility[i]
            final.append(posibility[i])
        i -= 1

    for i in range(len(final)):
        print(final[i], end="\n")


if __name__ == '__main__':

    print('Enter the cash : ')
    n = int(input())
    Fgreedy(n)
