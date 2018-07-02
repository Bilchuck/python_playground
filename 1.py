# factorial 6
def factorial(num): return 1 if num == 1 else factorial(num - 1) * num
factorial6 = factorial(6)
print("factorial6 = " + str(factorial6))

