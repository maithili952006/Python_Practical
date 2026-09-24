try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    assert num2 != 0, "Second number cannot be zero"

    result = num1 / num2

    if result < 0:
        raise ValueError("Result cannot be negative")

except ValueError as e:
    print("Value Error:", e)

except ZeroDivisionError as e:
    print("Zero Division Error:", e)

except AssertionError as e:
    print("Assertion Error:", e)

except Exception as e:
    print("General Exception:", e)

else:
    print("Division successful!")
    print("Result =", result)

finally:
    print("Program execution completed.")