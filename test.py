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

#age=(input('Age :'))
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
print(marks)