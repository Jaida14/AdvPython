# problem #1
# What is mising in the while loop?
# use a breakpoint in line 6 to debug
x = 1
while x < 10:
    print(x)
# it is missing a counter (doesn't need a break)
    x += 1


# problem #2
# use a breakpoint in line 14 to debug
mylist = list(range(5))  # not including

for x in range(1, 5):
    # for x in range(1, 6):
    print(f"Run No.:{mylist[x]}")
    # DOES need a print if using an fstring
    # meant to put all variables together without converting
    # range is too big when ending with 6
