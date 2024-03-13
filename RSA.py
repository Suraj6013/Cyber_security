import sympy
p=int(input("Enter the first prime number: "))
q=int(input("Enter the second prime number: "))
message = input("Enter the message: ")
decimal_message = int.from_bytes(message.encode(), 'big')
print(sympy.isprime(p))
print(sympy.isprime(q))
while p!=q:
    n=p*q
    t=(p-1)*(q-1)
    break
for i in range(2,t):
    #e=t-1
    e=0
    if e%t==0:
        e=i


d=pow(e, -1, t)

s=0
while True:
    if (s*e)%t==1:
        x=s
    break
c_text=0
if decimal_message<n:
    c_text=(decimal_message**e)%n
    decimal_message=(c_text**d)%n
    
print("cipher text: ",c_text)
decrypted_message = decimal_message.to_bytes((decimal_message.bit_length() + 7) // 8, 'big').decode()
print("decimal message: ", decimal_message)
print("decrypted message: ", decrypted_message)
