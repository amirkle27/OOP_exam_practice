
import time

def countdown(n):
    if n <= 0:
        time.sleep(0.5)
        print("🚀 Blast Off!")
        return
    time.sleep(0.5)
    print(n)
    countdown(n - 1)

def countup(n, num=1):
    if num > n:
        print("It's a Recursion!")
        return
    print(num)
    countup(n,num + 1)

def count_down_and_up(n, num=1):
    if n==num:
        print(n)
        return
    print(n)
    count_down_and_up(n-1,num)
    print(n)

def sum_recursion(n):
    if n==1:
        return 1
    return n + sum_recursion(n-1)


# sum_numbers(5) → 5 + sum_numbers(4)  (עוד לא יודעים כמה זה sum_numbers(4), אז עוצרים כאן!)
#   sum_numbers(4) → 4 + sum_numbers(3)
#     sum_numbers(3) → 3 + sum_numbers(2)
#       sum_numbers(2) → 2 + sum_numbers(1)
#         sum_numbers(1) → 1  ❗ כאן נעצר ❗
# 💥 עכשיו מתחילים לחזור חזרה ולחשב:
#
#         sum_numbers(1) → 1  ✅
#       sum_numbers(2) → 2 + 1 = 3  ✅
#     sum_numbers(3) → 3 + 3 = 6  ✅
#   sum_numbers(4) → 4 + 6 = 10  ✅
# sum_numbers(5) → 5 + 10 = 15  ✅

# 5 + sum_numbers(4)
# 4 + sum_numbers(3)
# 3 + sum_numbers(2)
# 2 + sum_numbers(1)

# 2 +             1 = 3
# 3 +             3 = 6
# 4 +             6 = 10
# 5 +            10 = 15

def factorial(n):
    #5*4*3*2*1
    if n==1:
        return 1
    return n* factorial(n-1)

   # 5 * factorial(5-1)
# print(factorial(5))

def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n//10)

print(sum_digits(9084))