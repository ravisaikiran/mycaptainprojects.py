fibSeries=[]
first=1
second=1
n=int(input("enter the number of terms:"))
while n>0:
    fibSeries.append(first)
    third=first+second
    first=second
    second=third
    n-=1
print(*fibSeries)
