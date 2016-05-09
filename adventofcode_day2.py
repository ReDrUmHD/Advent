inp = open("input.txt", "r")
area = 0
total = 0
ribbon_total = 0
for i in inp:
    x = i.split("x")
    l = int(x[0])
    w = int(x[1])
    h = int(x[2])
    area = 2*l*w + 2*w*h + 2*h*l
    ribbon_area = l*w*h
    side_one = l*w
    side_two = w*h
    side_three = h*l
    per_1 = l*2+w*2
    per_2 = l*2+h*2
    per_3 = w*2+h*2
    total += min(side_one, side_two, side_three)
    ribbon_total += min(per_1, per_2, per_3) + ribbon_area
    total += area
print(total)
print(ribbon_total)
