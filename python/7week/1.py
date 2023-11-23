cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

if len(cars) == 0 or len(cars) == 1:
    print(1)
elif len(cars) == 5:
    print(5)
elif len(cars) == 4:
    print(4)
else:
    print('not empty')

