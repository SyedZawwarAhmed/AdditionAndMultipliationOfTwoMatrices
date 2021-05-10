def print_matrix():
    print("RESULT:-")
    p = 0
    while p < len(g):
        q = 0
        while q < len(h):
            f = 0
            max_length = len(str(g[f][q]))
            while f < len(g):
                if max_length < len(str(g[f][q])):
                    max_length = len(str(g[f][q]))
                f += 1
            t = 0
            while t < max_length - len(str(g[p][q])):
                print(" ", end="")
                t += 1
            print(g[p][q], end="  ")
            q += 1
        print()
        p += 1

print("Enter Matrix A")
r = float(input("Enter number of ROWS: "))
c = float(input("Enter number of COLUMNS: "))

a = []
i = 0
while i < r:
    j = 0
    b = []
    while j < c:
        x = float(input("Enter number at A" + str(i + 1) + str(j + 1) + ": "))
        b.append(x)
        j += 1
    a.append(b)
    i += 1

print("Enter Matrix B")
r = float(input("Enter number of ROWS: "))
c = float(input("Enter number of COLUMNS: "))

z = []
i = 0
while i < r:
    j = 0
    y = []
    while j < c:
        x = float(input("Enter number at B" + str(i + 1) + str(j + 1) + ": "))
        y.append(x)
        j += 1
    z.append(y)
    i += 1

o = "Any Input"
while o != "A" and o != "a" and o != "M" and o != "m":
    o = input("PRESS (A/a) TO ADD OR PRESS (M/m) TO MULTIPLY THE MATRICES:- ")

if o == "A" or o == "a":
    # ADDITION
    if len(a) == len(z) and len(b) == len(y):
        g = []
        i = 0
        while i < r:
            j = 0
            h = []
            while j < c:
                x = a[i][j] + z[i][j]
                s = str(x)
                if s[-1] == "0" and s[-2] == ".":
                    x = int(x)
                h.append(x)
                j += 1
            g.append(h)
            i += 1
        print_matrix()
    else:
        print("Matrices can not be added")
elif o == "M" or o == "m":
    # MULTIPLICATION
    if len(a[0]) == len(z):
        g = []
        i = 0
        while i < len(a):
            j = 0
            h = []
            while j < len(z[0]):
                k = 0
                x = 0
                while k < len(a[0]):
                    n = a[i][k] * z[k][j]
                    x += n
                    k += 1
                s = str(x)
                if s[-1] == "0" and s[-2] == ".":
                    x = int(x)
                h.append(x)
                j += 1
            g.append(h)
            i += 1
        print_matrix()
    else:
        print("Matrices can not be multiplied")