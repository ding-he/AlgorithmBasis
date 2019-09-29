def print_time(n):
    print(n)
    if n <= 0:
        # 基线条件
        # 保证递归的结束条件
        print('end')
    else:
        # 递归条件
        # 是的递归能逐层分解
        print_time(n - 1)


def factorial(n):
    if n == 0 or n == 1:
        return 1;
    elif n < 0:
        return -1
    else:
        return n * factorial(n - 1)

print_time(100)
print(factorial(5))
