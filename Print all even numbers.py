start, end = map(int, input().split())

even_numbers = [str(num) for num in range(start, end + 1) if num % 2 == 0]
print(" ".join(even_numbers))
