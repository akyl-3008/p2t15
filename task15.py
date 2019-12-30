age = int(input("vozrast: "))
x = list(range(age))
if age % 2 == 0:
    print(x[2::2])
else:
    print(x[1::2])