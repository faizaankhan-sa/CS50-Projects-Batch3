from cs50 import get_int

while True:
    x = get_int("How high would you like your pyramid to be: ")
    if x > 0 and x < 9:
        break

for a in range(0, x, 1):
    for b in range(0, x, 1):
        if (a+b < x-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()