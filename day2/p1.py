n=897645
x=1
y=5
for i in range(x,y,1):
    if (x+y)%3==0:
        n=n//10
        print(n)
    elif (x+y)%2==0:
        n=n//100
        print(n)
        break
    x=x+1
    y=y-2
print(n)
print(x+y)
