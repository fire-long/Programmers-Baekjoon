n, m, k = map(int, input().split())

if n == 0:
  print(1)
else :
    data = list(map(int, input().split()))
    data.append(m)
    data.sort(reverse = True)
    index = data.index(m) + 1
    if index > k:
        print(-1)
    else:
        if n == k and m == data[-1]:
            print(-1)
        else:
            print(index)