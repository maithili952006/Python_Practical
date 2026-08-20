def greet_user(name="Guest"):
    return f"Hello, {name}!"

square = lambda x: x ** 2

if __name__ == "__main__":

    print(greet_user("Maithili"))
    num = 5
    print(f"The square of {num} is: {square(num)}")