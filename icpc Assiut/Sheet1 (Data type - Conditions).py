B)
a,s,d,f,g = input().split()
print(a,s,d,f,g ,sep="\n")
___________________________________
E)
from decimal import Decimal, ROUND_DOWN

a = float(3.141592653)
r= float(input())
area=r*r*a
asd = Decimal(str(area)).quantize(Decimal('.000000001'), rounding=ROUND_DOWN)

print(asd)
___________________________________
F)
a,b = input().split()
print(((int(a))%10)+((int(b))%10))
___________________________________
G)
n=int(input())
print(n*(n+1)//2)
___________________________________
H)
import math
def my_round(i):
  f = math.floor(i)
  return f if i - f < 0.5 else f+1

a,b = input().split()
x = float(int(a)/int(b))

print("floor "+str(a)+" / "+str(b)+" = "+str(math.floor(x)))
print("ceil "+str(a)+" / "+str(b)+" = "+str(math.ceil(x)))
print("round "+str(a)+" / "+str(b)+" = "+str(my_round(x)))
___________________________________
K)
a,s,d=input().split()

MAX= max(int(a),int(s),int(d))
MIN= min(int(a),int(s),int(d))
print(MIN,MAX)
___________________________________
M)
user_input = input()

try:
    val = int(user_input)
    print("IS DIGIT")

except ValueError:
        if user_input == user_input.capitalize():
            print("ALPHA")
            print("IS CAPITAL")

        elif user_input == user_input.lower():
            print("ALPHA")
            print("IS SMALL")
___________________________________
O)
x = input()

for i in range(len(x)):
    if str(x[i])=="+":
        z = x.split("+")
        print(int(z[0])+int(z[1]))

    elif str(x[i])=="*":
        z = x.split("*")
        print(int(z[0])*int(z[1]))

    elif str(x[i])=="-":
        z = x.split("-")
        print(int(z[0])-int(z[1]))

    elif str(x[i])=="/":
        z = x.split("/")
        print(int(z[0])/int(z[1]))

___________________________________
Q)
a,s = input().split()
if float(a)>0 and float(s)>0:
    print("Q1")
elif float(a)>0 and float(s)<0:
    print("Q4")
elif float(a)<0 and float(s)>0:
    print("Q2")
elif float(a)<0 and float(s)<0:
    print("Q3")
elif float(a)==0 and float(s)<0 or float(s)>0:
    print("Eixo Y")
elif float(s)==0 and float(a)<0 or float(a)>0:
    print("Eixo X")
elif float(a)==0 and float(s)==0:
    print("Origem")
___________________________________
T)
a1,s1,d1 = input().split()
a=int(a1)
s=int(s1)
d=int(d1)

maxx = int(max(a,s,d))
minn = int(min(a,s,d))

if a!=maxx and a!=minn:
    mid = a
    print(minn,a,maxx,sep="\n")

elif s!=maxx and s!=minn:
    mid = s
    print(minn,s,maxx,sep="\n")

elif d!=maxx and d!=minn:
    mid = d
    print(minn,d,maxx,sep="\n")

#_____________________________________________

elif a!= maxx and a == minn and a!=s and a!=d and s!=d:
    mid = a
    print(minn, a, maxx, sep="\n")

elif s!= maxx and s== minn and a!=s and a!=d and s!=d:
    mid = s
    print(minn, s, maxx, sep="\n")

elif d!= maxx and d== minn and a!=s and a!=d and s!=d:
    mid = d
    print(minn, d, maxx, sep="\n")
#_____________________________________________

elif a== maxx and a != minn and a!=s and a!=d and s!=d:
    mid = a
    print(minn, a, maxx, sep="\n")

elif s== maxx and s!= minn and a!=s and a!=d and s!=d:
    mid = s
    print(minn, s, maxx, sep="\n")

elif d== maxx and d!= minn and a!=s and a!=d and s!=d:
    mid = d
    print(minn, d, maxx, sep="\n")
#_____________________________________________

elif a==s==d:
    print(a,s,d, sep="\n")
#_____________________________________________

elif a==s== maxx :

    print(minn, maxx, maxx, sep="\n")

elif s==d== maxx :
    mid = s
    print(minn, maxx, maxx, sep="\n")

elif a==d== maxx:
    mid = s
    print(minn, maxx, maxx, sep="\n")

#_____________________________________________

elif a==s== minn :

    print(minn, minn, maxx, sep="\n")

elif s==d== minn:
    mid = s
    print(minn, minn, maxx, sep="\n")

elif a==d== minn:
    mid = s
    print(minn, minn, maxx, sep="\n")

print("")

print(a1,s1,d1, sep="\n")

__________________________________________________________________
U)
num = input()

try:
    c = num.split(".")
    if c[1] == "0" or c[1] == "00" or c[1] == "000":
     print("int "+c[0])

    else:
        z = num.split(".")
        print("float " + z[0] + " " + "0." + z[1])

except ValueError:

    print("error")
__________________________________________________________________
V)
a1,s,d1 = input().split()
a = int(a1)
d = int(d1)
if s==">":
    if a >d:
        print("Right")
    else:
        print("Wrong")

elif s=="<":
    if a <d:
        print("Right")
    else:
        print("Wrong")

elif s=="=":
    if a==d :
        print("Right")
    else:
        print("Wrong")
__________________________________________________________________
W)
a1,s,d1,k,f1 = input().split()
a = int(a1)
d = int(d1)
f = int(f1)
if s=="+":
    if a+d==f:
        print("Yes")
    else:
        print(a+d)

elif s=="-":
    if a-d==f:
        print("Yes")
    else:
        print(a-d)

elif s=="*":
    if a*d==f :
        print("Yes")
    else:
        print(a*d)

__________________________________________________________________
X)
l1,r1,l2,r2 = input().split()
l1 = int(l1)
r1 = int(r1)
l2 = int(l2)
r2 = int(r2)


if l1<l2 and l1<r2 and r1>l2 and r1>r2:
    print(str(l2)+" "+str(r2))

elif l1>l2 and l1<r2 and r1>l2 and r1<r2:
    print(str(l1)+" "+str(r1))
#_____________________________

elif l1<l2 and l1<r2 and r1>l2 and r1<r2 :
    print(str(l2)+" "+str(r1))

elif l1>l2 and l1<r2 and r1>l2 and r1>r2:
    print(str(l1)+" "+str(r2))
#____________________________________

elif l1<l2 and l1<r2 and r1==l2 and r1<r2:
    print(str(l2) + " " + str(r1))
elif l1>l2 and l1==r2 and r1>r2 and r1>l2:
    print(str(l1) + " " + str(r2))
#_____________________________

elif l1<l2 and l1<r2 and r1 == l2 and r1==r2:
    print(str(r1) + " " + str(r2))

elif l1==l2 and l1==r2 and r1>l2 and r1>r2:
    print(str(l2)+" "+str(l1))
#________________________________

elif l1==l2 and l1<r2 and r1 == l2 and r1 < r2:
    print(str(l2) + " " + str(l1))

elif l1>l2 and l1==r2 and r1>l2 and r1==r2:
    print(str(r1)+" "+str(r2))
#________________________________

elif l1<l2 and l1<r2 and r1>l2 and r1==r2:
    print(str(l2) + " " + str(r2))

elif l1==l2 and l1<r2 and r1>l2 and r1>r2:
    print(str(l2)+" "+str(r2))
#________________________________
elif l1>l2 and l1<r2 and r1>l2 and r1==r2:
    print(str(l1) + " " + str(r1))

elif l1==l2 and l1<r2 and r1>l2 and r1<r2:
    print(str(l1)+" "+str(r1))
#________________________________
elif l2==l1 and r2==r1 :
    print(str(l1)+" "+str(r1))
#____________________________________


else:
    print("-1")

__________________________________________________________________
y)
a1,s1,d1,f1 = input().split()
a=int(a1)
s=int(s1)
d=int(d1)
f=int(f1)
mul = a*s*d*f
mul1 = str(mul)
mul3 = mul1[-2:]
print(mul3)
_____________________________________________________________________
z)
import math
num1,pow1,num2,pow2 = input().split()
len_num1 = len(num1)
len_num2 = len(num2)
num11 = int(num1)
pow11 = int(pow1)
num22 = int(num2)
pow22 = int(pow2)

if ((math.log((num11)))*pow11) > ((math.log(num22))*pow22):
    print("YES")
else:
    print("NO")
_____________________________________________________________________

a,s = input().split()
a1 = int(a)
s1 = int(s)
if a1%s1==0 or s1%a1==0:
    print("Multiples")
else:
    print("No Multiples")
