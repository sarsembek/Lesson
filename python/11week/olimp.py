from mergeSort import mergeSort
a = [{20:"Sidorov"},{10:"Petrov"}, {15:"Ivanov"}]
keys = []
for x in a:
    keys.append(*x)
mergeSort(keys)
print(keys)


for i in range(len(keys)):
    for x in a:
        if list(x.keys())[0] == keys[i]:
            print(x.get(keys[i]))
            
