numbers = [12, 45, 7, 23, 56, 89, 34]

largest = max(numbers)
smallest = min(numbers)

sorted_numbers = sorted(numbers, reverse=True)
second_largest = sorted_numbers[1]

print("Largest Element:", largest)
print("Second Largest Element:", second_largest)
print("Smallest Element:", smallest)
