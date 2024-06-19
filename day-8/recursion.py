#fibbanoci
'''t=0

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fib(n-2)+fib(n-1)

if __name__=="__main__":
    n=int(input("enter  n"))
    print(fib(n))
    print(t)'''

#factorial
t=0    
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        t=+1
        return  n*fact(n-1)
    return t
if __name__=="__main__":
    n=int(input("enter  n"))
    print(fact(n))
    print(t)
       