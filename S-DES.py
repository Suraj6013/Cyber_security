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

# key generatiion part
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
print("key1: ",key1)
l, r = apply_two_bit_left_shift(l, r)
m = l + r
key2 = apply_p8_permutation(m)
print("key2: ",key2)

# encrycption part
plaintext = [1, 0, 0, 1, 0, 1, 1, 1]

# Initial permutation
def apply_ip8_permutation(m):
    key = []
    ip = [2, 6,3, 1, 4, 8, 5, 7]
    for i in range(len(ip)):
        c = ip[i]
        key.append(m[c-1])
    return key
after_ip = apply_ip8_permutation(plaintext)
print("after ip: ",after_ip) 

#divide into two parts
def divide_into_parts(after_ip):
    l = after_ip[0:4]
    r = after_ip[4:8]
    return l, r
l, r = divide_into_parts(after_ip)
print("l: ",l,"r: ",r)
l_initial=l #for xor operation we need l at the start
r_initial=r #for xor operation we need r at the start

#apply expansion permutation
def apply_ep(r):
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    key = []
    for i in range(len(ep)):
        c = ep[i]
        key.append(r[c-1])
    return key
expanded_r = apply_ep(r)
print("expanded r: ",expanded_r)

#apply xor operation
def apply_xor(expanded_r, key1):
    xor = []
    for i in range(len(expanded_r)):
        xor.append(expanded_r[i] ^ key1[i])
    return xor
xor = apply_xor(expanded_r, key1)
print("xor: ",xor)

#divide into two parts
def divide_into_parts(xor):
    l = xor[0:4]
    r = xor[4:8]
    return l, r
l, r = divide_into_parts(xor)
print("l: ",l,"r: ",r)

#apply s0 and s1 box
s0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

s1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def apply_s0(l):
    row = int(str(l[0])+str(l[3]), 2)
    col = int(str(l[1])+str(l[2]), 2)
    return s0[row][col]
def apply_s1(r):
    row = int(str(r[0])+str(r[3]), 2)
    col = int(str(r[1])+str(r[2]), 2)
    return s1[row][col]
s0_output = apply_s0(l)
s1_output = apply_s1(r) 

s0 = [int(i) for i in str(bin(s0_output))[2:]]
s1 = [int(i) for i in str(bin(s1_output))[2:]]  
s3 = s0 + s1
print("s-box combined: ",s3)

#apply p4 permutation
def apply_p4_permutation(s3):
    p4 = [2, 4, 3, 1]
    key = []
    for i in range(len(p4)):
        c = p4[i]
        key.append(s3[c-1])
    return key
p4 = apply_p4_permutation(s3)
print("p4: ",p4)

#apply xor operation
def apply_xor(l_initial, p4):
    xor = []
    for i in range(len(l_initial)):
        xor.append(l_initial[i] ^ p4[i])
    return xor
xor = apply_xor(l_initial, p4)
print("xor: ",xor)

#combine r and xor added in this order to escape swapping
combined = r_initial + xor
print("combined: ",combined)


