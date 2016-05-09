floor = list(input("Input your floors pls."))
dest = 0
first = 0

for i in enumerate(floor):
    if i[1] == "(":
        dest += 1
    elif i[1] == ")":
        dest -= 1
    else:
        print("Your string is incorrect!")
        break
    if dest < 0 and first != 1:
        print("%s causes santa to enter the basement" % (i[0] + 1))
        first = 1
print(dest)
