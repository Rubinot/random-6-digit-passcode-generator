import random

p = []
q = []
r = []
a_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s_y = ['!', '@', '#', '$', '%', '&']

def f():
    x = random.randint(0, 9)
    x_1 = random.choice(a_l)
    x_2 = random.choice(s_y)
    p.append(x)
    q.append(x_1)
    r.append(x_2)

for i in range(6):
    f()

p_a = []
c = []

def g(y):
    if c[y] == 1:
        p_a.append(str(p[y]))
    elif c[y] == 2:
        u = random.randint(1, 2)
        if u == 1:
            p_a.append(q[y])
        else:
            p_a.append(q[y].upper())
    else:
        p_a.append(r[y])

for y in range(6):
    x = random.randint(1, 3)
    c.append(x)
    g(y)

print(p_a[0] + p_a[1] + p_a[2] + p_a[3] + p_a[4] + p_a[5])
