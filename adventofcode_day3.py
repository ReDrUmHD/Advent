grid = []
inp = list(input("Please enter"))
var = ""
seen = set()
x = 0
y = 0
rx = 0
ry = 0
for i in enumerate(inp):
    if i[0] % 2 == 0 or i[0] == 0:
        if i[1] == ">":
            x += 1
        elif i[1] == "<":
            x -= 1
        elif i[1] == "^":
            y += 1
        elif i[1] == "v":
            y -= 1
        grid.append("%d, %d" % (x, y))
        seen.add("%d, %d" % (x, y))
    else:
        if i[1] == ">":
            rx += 1
        elif i[1] == "<":
            rx -= 1
        elif i[1] == "^":
            ry += 1
        elif i[1] == "v":
            ry -= 1
        grid.append("%d, %d" % (rx, ry))
        seen.add("%d, %d" % (rx, ry))
print(len(seen))