h,m = map(int,input().split())

totalm = 60 * h + m
totalm -= 45

if totalm > 0:
    h = int(totalm / 60)
    m = totalm - h*60
    print(h,m)
else:
    totalm += 24*60
    h = int(totalm / 60)
    m = totalm - h*60
    if h == 24: h = 0
    print(h,m)