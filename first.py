def middle(num1,num2):
    num1.extend(num2)
    num1.sort()
    l=len(num1)
    if l%2==1:
        return num1[l//2]
    else:
        return(num1[l//2-1]+num1[l//2])/2

num1=[1,2]
num2=[3]
print(middle(num1,num2))