#!/usr/bin/env python3
# while inp := input(" >> "):
#     eval(inp)


# inp = input()

# while inp:
#     eval(inp)
#     inp = input()


def trailing_zeroes(n):
    s = str(n)
    return len(s := str(n)) - len(s.rstrip("0"))


print(trailing_zeroes(00000567))
