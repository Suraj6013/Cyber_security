#key=[1,0,1,0,0,0,0,0,1,0]
#x=[3,5,2,7,4,10,1,9,8,6]
# p=[]
# #step-1: for p10 permutation
# for i in range(len(x)):
#     n=x[i]
#     p.append(key[n-1])
# print(p)
# #step-2 divide in to two parts  
# l=p[0:5]
# r=p[5:10]
# print(l)

# #step-3 aplly one bit left shift on each part
# m1 =l.pop(0)
# l.append(m1)
# print(l)
# m2 =r.pop(0)
# r.append(m2)
# print(r)
# m=l+r
# print("ls-1 combined",m)

# #step-4 apply p8 permutation
# key1=[]
# p8=[6,3,7,4,8,5,10,9]
# for i in range(len(p8)):
#     c=p8[i]
#     key1.append(m[c-1])
# print("key1:",key1)

# #step-5 apply two bit left shift on each part
# for i in range(0,2):
#     m1 =l.pop(0)
#     l.append(m1)
#     m2 =r.pop(0)
#     r.append(m2)
# m=l+r
# print("ls-2 combined",m)

# #step-6 apply p8 permutation
# key2=[]
# for i in range(len(p8)):
#     c=p8[i]
#     key2.append(m[c-1])
# print("key2:",key2)

def p10_permutation(key):
    p = []
    x = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    for i in range(len(x)):
        n = x[i]
        p.append(key[n-1])
    return p

def divide_into_parts(p):
    l = p[0:5]
    r = p[5:10]
    return l, r

def apply_one_bit_left_shift(l, r):
    m1 = l.pop(0)
    l.append(m1)
    m2 = r.pop(0)
    r.append(m2)
    return l, r

def apply_p8_permutation(m):
    key = []
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    for i in range(len(p8)):
        c = p8[i]
        key.append(m[c-1])
    return key

def apply_two_bit_left_shift(l, r):
    for i in range(0, 2):
        m1 = l.pop(0)
        l.append(m1)
        m2 = r.pop(0)
        r.append(m2)
    return l, r

# Example usage:
key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
p = p10_permutation(key)
l, r = divide_into_parts(p)
l, r = apply_one_bit_left_shift(l, r)
m = l + r
key1 = apply_p8_permutation(m)
print(key1)
l, r = apply_two_bit_left_shift(l, r)
m = l + r
key2 = apply_p8_permutation(m)
print(key2)
