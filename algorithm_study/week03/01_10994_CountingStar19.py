
def fillStar(arr, n, x, y):

    if n == 1:
        arr[y][x] = '*'
        return

    size = 4*n-3
    for i in range(size):
        arr[y][x+i] = '*'
        arr[y+i][x] = '*'
        arr[y+size-1][x+i] = '*'
        arr[y+i][x+size-1] = '*'
        
    fillStar(arr, n-1, x+2, y+2)
    

def printStar(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end='')
        print()

n = int(input())
size = 4*n-3
starList = [[' ']*size for _ in range(size)]
fillStar(starList, n, 0, 0)
printStar(starList)
