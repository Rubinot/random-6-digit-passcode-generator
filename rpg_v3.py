import random

p_a = []
c = []
p = []
q = []
r = []
a_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s_y = ['!', '@', '#', '$', '%', '&']

try:
    z = int(input("Digits in the password: "))
    for i in range(z):  # first for loop
        p.append(random.randint(0, 9))
        q.append(random.choice(a_l))
        r.append(random.choice(s_y))
    
    for y in range(z):
        x = random.randint(1, 3)
        c.append(x)
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
    
    print(''.join(p_a))

except:
    print("Enter a proper number")
