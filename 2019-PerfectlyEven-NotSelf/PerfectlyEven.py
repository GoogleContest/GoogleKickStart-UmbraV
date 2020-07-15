T = int(input())    # Number of Test Cases

for i in range(T):
    N = str(input())  # The actual number, using a string to better manipulate
    Digits = len(N)  # How many digits are there in the number
    IsEven = True

    # Find the first odd digit
    for index in range(Digits):
        if (int(N[index]) % 2 != 0):
            OddIndex = index  # ! New variable
            IsEven = False  # Update to show that it's not even
            break

    if (IsEven == True):
        print("Case #{}: {}".format(int(i + 1), 0))
    elif (Digits == 1):
        print("Case #{}: {}".format(int(i + 1), 1))
    elif (N[OddIndex] == "9"):
        N[OddIndex] = "8"
        Even = N[:OddIndex] + "8" * (Digits - 1 - OddIndex)
        difference = int(N) - int(Even)
        print("Case #{}: {}".format(int(i + 1), difference))
    else:
        if (OddIndex != 0):
            # Get the increments
            Up = int(N[OddIndex]) + 1
            N[OddIndex] = str(Up)
            Plus = N[:OddIndex] + "0" * (Digits - 1 - OddIndex)

            # Get the decrements
            Down = int(N[OddIndex]) - 1
            N[OddIndex] = str(Down)
            Minus = N[:OddIndex] + "8" * (Digits - 1 - OddIndex)

            # Get the smaller of the 2 values
            difference = min(int(Plus) - int(N), int(N) - int(Minus))

            print("Case #{}: {}".format(int(i + 1), difference))
        else:
            # Get the increments
            Up = int(N[OddIndex]) + 1
            N[OddIndex] = str(Up)
            Plus = N[OddIndex] + "0" * (Digits - 1 - OddIndex)

            # Get the decrements
            Down = int(N[OddIndex]) - 1
            N[OddIndex] = str(Down)
            Minus = N[OddIndex] + "8" * (Digits - 1 - OddIndex)

            # Get the smaller of the 2 values
            difference = min(int(Plus) - int(N), int(N) - int(Minus))

            print("Case #{}: {}".format(int(i + 1), difference))


    





