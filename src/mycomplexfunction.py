def another_function(y):
    if y > 0:
        for i in range(y):
            if i % 2 == 0:
                if i % 3 == 0:
                    print(f"{i} is divisible by 2 and 3")
                else:
                    print(f"{i} is divisible by 2 but not by 3")
            else:
                if i % 3 == 0:
                    print(f"{i} is divisible by 3 but not by 2")
                else:
                    print(f"{i} is not divisible by 2 or 3")
    else:
        print("y is not positive")

another_function(5)