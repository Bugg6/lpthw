# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i += 1
#     print("Numbers is now: ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
# for num in numbers:
#     print(num)


def print_while(num, inc):
    i = 0
    numbers = []

    while i < num:
         print(f"At the top i is {i}")
         numbers.append(i)

         i += inc
         print("Numbers is now: ", numbers)
         print(f"At the bottom i is {i}")

print_while(11, 2)
