def sum_two_smallest_numbers(numbers):
    list.sort(numbers)
    return numbers[0] + numbers[1]

print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))