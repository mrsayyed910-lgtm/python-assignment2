def count_frequency(arr):
    frequency = {}

    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    for key, value in frequency.items():
        print(f"{key} -> {value} times")

arr = [1, 2, 2, 3, 1, 4, 2]
count_frequency(arr)
