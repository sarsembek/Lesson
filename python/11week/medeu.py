from mergeSort import mergeSort
a = [41,40,39,42]
b = [42,41,42,37,40]
cnt = 0
mergeSort(a)
print(a)
for x in b:
    for y in a:
        if y >= x:
            cnt += 1
            a.remove(y)

print(cnt)