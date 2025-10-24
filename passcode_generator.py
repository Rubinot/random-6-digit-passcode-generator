import random

p = []
q = []
r_1 = []
i_n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s_y = ['!', '@', '#', '$', '%', '&']

for i in range(6):
    x = random.choice(i_n)
    p.append(x)


for i in range(6):
    x = random.choice(a_l)
    q.append(x)


for i in range(6):
    x = random.choice(s_y)
    r_1.append(x)


p_a = []
c = []  # chooser
for i in range(6):
    x = random.randint(1, 3)
    c.append(x)


# for the first digit:
if c[0] == 1:
    p_a.append(p[0])
    
elif c[0] == 2:
    u = random.randint(1, 2)
    if u == 1:
        p_a.append(q[0])
        
    else:
        p_a.append(q[0].upper())
        
else:
    p_a.append(r_1[0])
    
# for the second digit:
if c[1] == 1:
    p_a.append(p[1])
    
elif c[1] == 2:
    u = random.randint(1, 2)
    if u == 1:
        p_a.append(q[1])
        
    else:
        p_a.append(q[1].upper())
        
else:
    p_a.append(r_1[1])
    

# for the third digit:
if c[2] == 1:
    p_a.append(p[2])
    
elif c[2] == 2:
    u = random.randint(1, 2)
    if u == 1:
        p_a.append(q[2])
        
    else:
        p_a.append(q[2].upper())
        
else:
    p_a.append(r_1[2])
    

# for the fourth digit:
if c[3] == 1:
    p_a.append(p[3])
    
elif c[3] == 2:
    u = random.randint(1, 2)
    if u == 1:
        p_a.append(q[3])
        
    else:
        p_a.append(q[3].upper())
        
else:
    p_a.append(r_1[3])
    

# for the fifth digit:
if c[4] == 1:
    p_a.append(p[4])
    
elif c[4] == 2:
    u = random.randint(1, 2)
    if u == 1:
        p_a.append(q[4])
        
    else:
        p_a.append(q[4].upper())
        
else:
    p_a.append(r_1[4])
    

# for the sixth digit:
if c[5] == 1:
    p_a.append(p[5])
    
elif c[5] == 2:
    u = random.randint(1, 2)
    if u == 1:
        p_a.append(q[5])
        
    else:
        p_a.append(q[5].upper())
        
else:
    p_a.append(r_1[5])
    
print(p_a[0] + p_a[1] + p_a[2] + p_a[3] + p_a[4] + p_a[5])