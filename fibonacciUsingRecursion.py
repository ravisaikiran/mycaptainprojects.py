def fib(first,second,n):
    if n>0:
        fibSeries.append(first)
        third=first+second
        first=second
        second=third
        n-=1
        return fib(first,second,n)
    else:
        return fibSeries
fibSeries=[]
first=1
second=1
n=int(input("enter the number of terms:"))
print(*fib(first,second,n))
