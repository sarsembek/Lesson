foot = int(input())
sizes = list(map(int,input().split()))

count = 0

if sizes[0] >= foot:
    foot = sizes[0]
    count = 1
    sizes.remove(sizes[0])

for size in sizes:
    if size - foot >= 3:
        foot = size
        count += 1

print(count)
