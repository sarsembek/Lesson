def sum_range(start, end):
    if start > end:
        start, end = end, start

    result = sum(range(start, end + 1))

    return result


start, end = 1, 100
result = sum_range(start, end)

print(f"The result is: {result}")


