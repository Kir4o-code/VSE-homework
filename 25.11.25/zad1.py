def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total

def sum_list_rec(nums):
    if not nums:
        return 0
    return nums[0] + sum_list_rec(nums[1:])

def reverse_string(s):
    return s[::-1]

def reverse_string_rec(s):
    if len(s) <= 1:
        return s
    return reverse_string_rec(s[1:]) + s[0]

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
