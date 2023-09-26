# for
names=['a','b','c','d']
for name in names:
    print(name)

sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum+=x

print(sum)

a=list(range(100))
print(a)

# while
n=99
while n>=0:
    n=n-1
print(n)

# break
n=0
while n<100:
    if(n>=10):
        break
    n+=1
print(n)

# contiune
n=0
while n<10:
    n+=1
    if(n%2==0):
        continue
print(n)