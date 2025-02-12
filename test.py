#Slicing
#Break the string
'''string = "hello, World!"
print(len(string))
print(string[-3:-1])  # Output: Hello
print(string.endswith("d"))
print(string.capitalize())
print(string.replace("l","a"))
print(string)
print(string.find("W"))
print(string.count("l"))'''

'''def f(x):
    d=0
    y=1
    while y <= x:
        d=d+1
        y=y*3
    return(d)

print(f(8538))'''

'''def h(n):
    s = 0
    for i in range(1,n+1):
        if n%i > 0:
           s = s+1
    return(s)
print(h(61)-h(60))  # Output: 4
print(h(60))  # Output: 4'''

'''#age=(input('Age :'))
#print (age)  # Output: Age :
marks=[11,22,143 ,15,19,17]
print(marks)
print(type(marks))
print(marks[2])
#marks[2]="Suthar"
print(marks[2])
#print(marks[2:5])
#marks.append("Hello")
marks.reverse()
#print(marks.sort())
marks.pop(2)
print(marks)'''

'''movies=[]
mov1=input("Enter Movie :")
mov2=input("Enter Movie :")
mov3=input("Enter Movie :")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)'''

'''list1=[1,2,1]
list2=[3,5,6]
copylist2=list2.copy()
copylist2.reverse()
if (copylist2==list1):
        print("True") 
else:
       print("False")'''

'''n=int(input("Enter a number : "))
for i in range(1,n+1):
     if (n%i==0):
        print(i,"is a factor")'''

'''def factor(x):
    if(x==1):
        return 1
    else:
        return x*factor(x-1)
    
n=int(input("Enter a number : "))
print("Factorial of",n,"is",factor(n))  # Output: Factorial of'''

'''def prime(x):
    if(x==1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
        return True
n=int(input("Enter a number to check prime or not : "))
print("Prime or not",prime(n))  # Output: Prime or not'''
   
def isprime(x):
    if(x==1):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def prime(n):
    (count,i,plist)=(0,1,[])
    if(n==1):
        return False
    
    else:
        while count<n:
            if isprime(i):
                (count,plist)=(count+1,plist+[i])
            i+=1
    return plist

n=int(input("Enter range to check prime numbers : "))
print("This are the ",n,"Prime numbers ",prime(n))




