from math import factorial 

def total_ways(a, b, c, d): 
 return factorial(a+b+c+d)//(factorial(a)*factorial(b)*factorial(c)*factorial(d)) 

def g(a, b, c, d, n): 
    if a==0 and b==0 and c==0 and d==0: 
        return '' 
    ways=total_ways(a, b, c, d) 

    if n <= (ways*a)//(a+b+c+d) and a>0: ##letter is 'A' 
        return 'A'+g(a-1, b, c, d, n) 

    if n <= (ways*(a+b))//(a+b+c+d) and b>0: ##letter is 'B' 
        return 'B'+g(a, b-1, c, d, n-(ways*a)//(a+b+c+d)) 

    if n <= (ways*(a+b+c))//(a+b+c+d) and c>0: ##letter is 'C' 
        return 'C'+g(a, b, c-1, d, n-(ways*(a+b))//(a+b+c+d))

    else: ##letter is 'D' 
        return 'D'+g(a, b, c, d-1, n-(ways*(a+b+c))//(a+b+c+d)) 

a=int(input('Enter value for a >';)) 
b=int(input('Enter value for b >';)) 
c=int(input('Enter value for c >';)) 
d=int(input('Enter value for d >';)) 
n=int(input('Enter value for n >';)) 

print(g(a, b, c, d, n))