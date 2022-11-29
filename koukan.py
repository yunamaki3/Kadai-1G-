a = [13, 29, 41, 75, 69, 120, 203, 41, 52, 32]

def babble_sort(arr):
    N = len(arr)
    for i in range(N-1):
        cnt = 0
        for j in range(0, N-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt = cnt + 1
        if cnt == 0:
            return arr
    return arr

b = babble_sort(a)
print("番号 データ")
for i in range(len(b)):
  print(i+1,b[i])
