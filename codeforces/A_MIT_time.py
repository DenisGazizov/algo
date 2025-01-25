data = [5]
while data[-1] < 1000000000:
    data.append(data[-1] * 5)
for _ in range(int(input())):
    x = int(input())
    if x <= 5:
        print('MIT time')
    else:
        l, r = 0, len(data) - 1
        while l != r:
            mid = (r + l) // 2
            if data[mid] == x:
                print(f'MIT^{mid + 1} time')
                break
            elif x < data[mid]:
                if x > data[mid-1]:
                    print(f'MIT^{mid + 1} time')
                    break
                else:
                    r = mid
            else:
                if x <= data[mid+1]:
                    print(f'MIT^{mid+2} time')
                    break
                else:
                    l = mid + 1


