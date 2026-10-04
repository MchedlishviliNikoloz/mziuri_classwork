def is_even(number: int) -> bool:
    return number % 2 == 0

def sum_of_list(lsit) -> int:
    sum = 0
    for i in lsit:
        sum += i
    return sum

print(is_even(4))
print(sum_of_list([1,2,3,4,5]))