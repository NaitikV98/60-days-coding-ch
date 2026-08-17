
numbers = [10, 20, 10, 30, 20, 10, 40]


total = 0
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    total += num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Numbers:", numbers)
print("Sum:", total)
print("Max:", maximum)
print("Min:", minimum)



frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)



reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed List:", reversed_list)