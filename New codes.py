# List Compression

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

print("number_power_2")