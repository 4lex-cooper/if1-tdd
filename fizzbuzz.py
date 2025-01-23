def fizzbuzz(input_value):
    if input_value % 3 == 0 and input_value % 5 == 0:
        return "fizzbuzz"
    elif input_value % 3 == 0:
        return "fizz"
    elif input_value % 5 == 0:
        return "buzz"
    else:
        return input_value


for i in range(1, 101):
    print(fizzbuzz(i))
