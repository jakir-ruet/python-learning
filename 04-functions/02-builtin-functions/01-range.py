# range(start, stop, step)
a = range(2, 6)
for n in a:
    print("without step", n)

b = range(2, 9, 2)
for m in b:
    print("with step", m)

c = range(20, 3, -2)
for o in c:
    print("with - step", o)
