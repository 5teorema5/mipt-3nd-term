numbers = input()
numbers = numbers.split()
numbers = [int(numbers[i]) for i in range(len(numbers))]
print(max(numbers) - min(numbers))
