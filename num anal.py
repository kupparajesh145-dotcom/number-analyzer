num = int(input("enter a num:"))

#count digits
temp = num
count=0
while temp > 0:
    temp=temp//10
    count=count+1
print("count=",count)
#sum of digits
temp=num
total=0
for i in range(1,temp+1):
    total=total+temp
print("sum=",total)

#reverse num
temp=num
rev=0
while temp > 0:
    digit=temp % 10
    rev=rev*10+digit
    temp=temp//10

print("reverse=",rev)