import random
key=[1,0,1,0,0,0,0,0,1,0]
x=[3,5,2,7,4,10,1,9,8,6]
p=[]
for i in range(len(x)):
    n=x[i]
    p.append(key[n-1])
print(p)

l=p[0:5]
r=p[5:10]
print(l)
m1 =l.pop(0)
l.append(m1)
print(l)
m2 =r.pop(0)
r.append(m2)
print(r)
m=l+r
print(m)
new_l=[]
p8=[6,3,7,4,8,5,10,9]
for i in range(len(p8)):
    c=p8[i]
    new_l.append(m[c-1])
m1 =l.pop(0)
l.append(m1)
print(l)
m2 =r.pop(0)
r.append(m2)
print(r)
m=l+r