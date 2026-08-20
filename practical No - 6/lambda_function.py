def square_standard(x):
    return x ** 2

square_lambda = lambda x: x ** 2

multiply = lambda a, b: a * b

print("Square using standard function:", square_standard(5))
print("Square using lambda function:  ", square_lambda(5))
print("Multiplication using lambda:   ", multiply(4, 6))