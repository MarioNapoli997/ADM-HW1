#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Introduction

## PROBLEM 1


# In[1]:


## 1) Say "Hello, World!" With PythonSay "Hello, World!" With Python

print("Hello, World!")


# In[4]:


## 2) Python If-ElsePython If-Else

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0 or n>= 6 and n<=20:
        print("Weird")
    else:
        print("Not Weird")


# In[5]:


## 3) Arithmetic Operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# In[6]:


## 4) Python:Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# In[7]:


## 5) Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)


# In[11]:


## 6) Write a function

def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True  
    return leap

year = int(input())
print(is_leap(year))


# In[12]:


## 7) Print function

if __name__ == '__main__':
    n = int(input())
    s=""
    for i in range (1,n+1):
        s+=str(i)
    print(s)


# In[ ]:


## Data Types 


# In[13]:


## 8) List comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = [a for a in range (0,x+1)]
    j = [a for a in range (0,y+1)]
    k = [a for a in range (0,z+1)]
    
    newlist = [[x, y, z] for x in i for y in j for z in k if x+y+z != n]
    
    print(newlist)


# In[14]:


## 9) Find the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n>= 2 and n<=10:
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        for z in student_marks.keys():
            if len(student_marks[z]) == 3:
                for y in range(0,len(student_marks[z])):
                   if student_marks[z][y]>100 or student_marks[z][y]<0:
                       raise ValueError("marks value must be included between 0 and 100")
            else:
                raise ValueError("length of marks array must be equal to 3")
                        
        a = 0
        c = 0
        for i in student_marks.keys():
           if i == query_name:
               for x in student_marks[i]:
                    a+=x
                    c+=1
        print("{:.2f}".format(a/c))      
    else:
       raise ValueError("n must be included between 2 and 10")


# In[16]:


## 10) Nested Lists

if __name__ == '__main__':
    a = list()
    b = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        b.append(name)
        a.append(score)
    c = 0
    m = 0
    while a[c]==min(a) and c<len(a)-1:
        c+=1
    m = a[c]
    result = list()
    
    for i in a:
        if i == m:
            result.append(i) 
        else:    
            if i < m and i > min(a):
                m = i
                result = list()
                result.append(m)
    resultfin = list()
    for x in range(0,len(a)):
        if a[x]==m:
            resultfin.append(b[x])
            
    resultfin=sorted(resultfin)
    for i in resultfin:
        print(i)


# In[17]:


## 11) Find the Runner-Up Score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=list(arr)
    c=0
    while a[c]==max(a) and c<=len(a)-1:
        c+=1
    ru=a[c]
    for i in range(1,len(a)):
        if a[i]>ru and a[i]<max(a):
            ru=a[i]
            
   
    print(ru)
        


# In[18]:


## 12) Lists

if __name__ == '__main__':
    N = int(input())
    istr = list()
    a=list()
    b=list()
    for _ in range(N):
            istr.append(input().split())
            
    
    for i in range(0,len(istr)):
        if istr[i][0]=="insert":
            a.insert(int(istr[i][1]),int(istr[i][2]))
        if istr[i][0]=="print":
            print(a)   
        if istr[i][0]=="sort":
            a.sort()
        if istr[i][0]=="reverse":
            a.reverse()
        if istr[i][0]=="append":
            a.append(int(istr[i][1]))
        if istr[i][0]=="remove":
            a.remove(int(istr[i][1]))
        if istr[i][0]=="pop":
            a.pop()


# In[31]:


## 13) Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla=tuple(integer_list)
    print(hash(tupla))


# In[ ]:


## String


# In[33]:


## 14) sWAP cASE

def swap_case(s):

    a = "abcdefghijklmnopqrstuvwxyz"
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    snuovo=""
    for i in s:
        if i in A:
            snuovo+=i.lower()
        if i in a:
            snuovo+=i.upper()
        if i not in a and i not in A: 
            snuovo+=i
    return snuovo

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[34]:


## 15) String Split and Join

def split_and_join(line):
    line=line.split()
    a = "-".join(line)
    return a 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[39]:


## 16) What's Your Name?

def print_full_name(first, last):
    # Write your code here
    a = "Hello "
    a+= first
    a+=" "
    a+= last
    a+="! You just delved into python."
    print (a)
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[41]:


## 17) Mutuations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
   
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[43]:


## 18) Find a string

def count_substring(string, sub_string):

    c = 0
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string):
            c += 1

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[44]:


## 19) String Validators 

if __name__ == '__main__':
    s = input()

    alphanum=alpha=digit=lower=upper=0
    for i in s:
        if i.isalnum():
            alphanum+=1
        if i.isalpha():
            alpha+=1
        if i.isdigit():
            digit+=1
        if i.islower():
            lower+=1
        if i.isupper():
            upper+=1
      
    print(alphanum>0)
    print(alpha>0)
    print(digit>0)  
    print(lower>0)  
    print(upper>0)      


# In[45]:


## 20) Text Alignment 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[47]:


## 21) Text Wrap

def wrap(string, max_width):
    if len(string)>0 and len(string)<1000:
        if max_width>0 and max_width < len(string):
            n=x=0
            result=""
            while n < len(string)-1:
                n+=max_width
                result+=string[x:n]
                x=n
                result+="\n" 
        else:
            raise ValueError("width must be included between o and len s") 
    else: 
        raise ValueError("len must be included between 0 and 1000")     
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[49]:


## 22) Designer Door Mat 

N, M = map(int,input().split())

pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]
print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))


# In[51]:


## 23) Strimng Formatting

def print_formatted(number):
    # your code goes here
    
    width=len(bin(number))-2
    for i in range(1,number+1): 
        for x in ('d', 'o', 'X', 'b'):
            print("{0:{width}{x}}".format(i, x=x, width=width), end=' ')
        print()
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[53]:


## 24) Alphabet Rangoli

def print_rangoli(size):

    # your code goes here
    a = "abcdefghijklmnopqrstuvwxyz"
    d = [a[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for x in items:
        t = d[-(x+1):]
        r = t[::-1]+t[1:]
        print("-".join(r).center(n*4-3, "-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[57]:


## 25) Capitalize!

import os

def solve(s):

    s=s.split(" ")
    result=""
    for i in s:
        for x in range(0,len(i)):
            if x==0:
                result+=i[0].upper()
            else:
                result+=i[x]
        result+=" "
   
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


# In[60]:


## 26) The Minione Game 

def minion_game(string):

    v="aeiouAEIOU"
    cons=0
    voc=0
    for i in range(0,len(string)):
        if string[i] in v:
            voc+=len(string)-i
        else:
            cons+=len(string)-i
    
    if cons>voc:
        print("Stuart",cons)
    elif voc>cons:
        print("Kevin",voc)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[62]:


## 27) Merge the Tools 

def merge_the_tools(string, k):
    if len(string)>0 and len(string)<=10**4:
        if k>=1 and k<=len(string):
            div = (len(string)//k)
            pos=0
            incremento=k
            while pos<len(string):
                res=""
                res+=string[pos:k]
                pos=k
                k+=incremento
                uniqueres=res[0]
                for i in res:
                    if i not in uniqueres:
                        uniqueres+=i
                print(uniqueres)
                
                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# In[ ]:


## Sets


# In[64]:


## 28) Introduction to Sets

def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[65]:


## 29) Symmetric Difference

m = int(input())
a = input()
n = int(input())
b = input()

a = a.split()
a = set(list(map(int, a)))
b = b.split()
b = set(list(map(int, b)))



r1 = a.difference(b)
r2 = b.difference(a)
r = sorted(set.union(r1, r2))



for i in r:
    print(i, "\t")


# In[67]:


## 30) Set.add()

a = set()
[a.add(input()) for _ in range(int(input()))]
print(len(a))


# In[68]:


## 31) Set.discard(),remove(),pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
istr=list()

for _ in range(N):
    istr.append(input().split())

for i in range(0, len(istr)):
    if istr[i][0] == "discard":
        s.discard(int(istr[i][1]))
    if istr[i][0] == "remove":
        s.remove(int(istr[i][1]))
    if istr[i][0] == "pop":
        s.pop()
        
print(sum(s))


# In[69]:


## 32) Set.union() Operation

m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))

res=s1.union(s2)
print(len(res))


# In[70]:


## 33) Set.intersection() Operation

m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))
res = s1.intersection(s2)

print(len(res))


# In[71]:


## 34) Set.difference() Operation

m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))
res = s1.difference(s2)

print(len(res))


# In[72]:


## 35) Set.symmetric_difference() Operation

m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))
res = s1.symmetric_difference(s2)

print(len(res))


# In[73]:


## 36) Set Mutations

n = int(input())
s = set(map(int, input().split()))
N = int(input())
istr=list()





for _ in range(N):
    istr, _ = input().split()
    s2 = set(map(int, input().split()))
    if(istr == "intersection_update"):
        s.intersection_update(s2)
    elif(istr == "update"):
        s.update(s2)
    elif(istr == "symmetric_difference_update"):
        s.symmetric_difference_update(s2)
    elif(istr == "difference_update"):
        s.difference_update(s2)



print(sum(s))


# In[74]:


## 37) The Captain's Room

n = int(input())
e = list(map(int, input().split()))
p = set()
d = set()
e.sort()
for i in range(0,len(e),2):
    p.add(e[i])
for x in range(1,len(e),2):
    d.add(e[x])
    
print(p.symmetric_difference(d).pop())


# In[75]:


## 38) Chek Subset

n = int(input())

for _ in range(n):
    N = int(input())
    sub = set(map(int, input().split()))
    M = int(input())
    s = set(map(int, input().split()))
    print (sub.issubset(s) )


# In[76]:


## 39) Check Strict Superset

sup = set(map(int, input().split()))
n = int(input())
c=0
for _ in range(n):
    s = set(map(int, input().split()))
    if sup.issuperset(s):
        c+=1
        
print(c==n)


# In[77]:


## 40) No Idea!

n = input().split(' ')
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

h = 0
for i in arr:
    if i in A:
        h += 1
    if i in B:
        h -= 1

print(h)


# In[ ]:


## Collections


# In[78]:


## 41) collections.Counter()

from collections import Counter

n = int(input())
l = list(map(int, input().split()))
N = int(input())
c = list()
res = 0
for _ in range(N):
    e = list(map(int, input().split()))
    c.append(e)
    
for i in range(0,N):
    if c[i][0] in l:
        res+=c[i][1]
        l.remove(c[i][0])
        
print(res)


# In[79]:


## 42) DefaultDict Tutorial

from collections import defaultdict
d = defaultdict(list)
n, m = map(int,input().split())

for i in range(1, n+1):
    d[input()].append(str(i))
for i in range(m):
    b = input()
    if b in d:
        print(' '.join(d[b]))
    else:
        print(-1)


# In[81]:


## 43) Collections.namedtuple()

from collections import namedtuple
n = int(input())
col = ",".join(input().split())
S = namedtuple("Student", col)
num = 0

if n > 0 and n <= 100:
    for i in range(n):
        row = input().split()
        stud = S(*row)
        num += int(stud.MARKS)
    print(num/n)
else:
    raise ValueError("n must be includeed between 0 and 100")


# In[82]:


## 44) Collections.OrderedDict()

from collections import OrderedDict

n = int(input())
s = OrderedDict()



if n > 0 and n <= 100:
    for i in range(n):
        item = input().split()
        price = int(item[-1])
        item_name = " ".join(item[:-1])
        if s.get(item_name):
            s[item_name] += price
        else:
            s[item_name] = price
    for i, j in s.items():
        print(i, j)
else:
    raise ValueError("n must be includeed between 0 and 100")


# In[84]:


## 45) Collections.deque()

from collections import deque

n = int(input())

res = deque()
for _ in range(n):
    i = list(input().split())
    if i[0] == "append":
        res.append(i[1])
    if i[0] == "appendleft":
        res.appendleft(i[1])
    if i[0] == "pop":
        res.pop()
    if i[0] == "popleft":
        res.popleft()
print(*res, sep = " ")


# In[85]:


## 46) Piling Up!

for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")


# In[86]:


## 47) Company Logo

import math
import os
import random
import re
import sys
from collections import OrderedDict



if __name__ == '__main__':
    s = str(input())
    d = dict()
    c=0
    for i in sorted(set(s)):
        d[i]=s.count(i)   
    sortedDict = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse = True))
    
    
    res = list(sortedDict.keys())

    
    count=0
    while count < 3: 
        print(res[count], sortedDict[res[count]])
        count+=1


# In[87]:


## 48) Word Order

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())


# In[ ]:


## Date and Time


# In[88]:


## 49) Calendar Module

import calendar as ca
d,m,y = ([int(i) for i in input().split(' ')])
a = ca.weekday(y,d,m)
n = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print (n[a])


# In[89]:


## 50) Time Delta

import math
import os
import random
import re
import sys
import datetime



# Complete the time_delta function below.
def time_delta(t1, t2):
    first = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(abs(int((first-second).total_seconds())))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


# In[ ]:


## Exceptions


# In[92]:


## 51) Exceptions

n = int(input())



for i in range(n):
    try:
        a,b= map(int,input().split())
        print(a//b)
    except BaseException as s:
        print("Error Code:", s)


# In[ ]:


## Built-In


# In[93]:


## 52) Zipped!

n, x = map(int, input().split())



res = []
for i in range(x):
    res.append( map(float, input().split()))



for i in zip(*res):
    print(sum(i) / x) 


# In[94]:


## 53) Athlete Sort

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    num = input().split()
    a = int(num[0])
    b = int(num[1])
    arr = []
    for _ in range(a):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    res = sorted(arr, key = lambda x: x[k])
    for i in res:
        print(*i)


# In[95]:


## 54) ginortS

s = input()



res = []
even = []
odd = []
for i in s:
    if i.islower() or i.isupper():
        res.append(i)
        res = res[::-1]
        res.sort(key = lambda i:(not i.islower(), i))
    if i.isdigit():
        if int(i) % 2 != 0:
            odd.append(i)
        if int(i) % 2 == 0:
            even.append(i)



for i in res:
    print(i, end = "")
for i in sorted(odd):
    print(i, end = "")
for i in sorted(even):
    print(i, end = "")


# In[ ]:


## Python Functionals


# In[97]:


## 55) Map and Lambda Function

cube = lambda x: pow(x, 3)



def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    seq = [0,1]
    for i in range(2, n):
        num = seq[-1] + seq[-2]
        seq.append(num)
    return seq

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# In[ ]:


## Regex and Parsing challenges


# In[98]:


## 56) Detect Floating Point Number

def is_float(txt):
    try:
        float(txt)
        return True
    except ValueError:
        return False

n = int(input())
lines = [input().strip() for _ in range(n)]
for l in lines:
    if(l=='0'): print(False)
    else:
        print(is_float(l))


# In[100]:


## 57) Re.split()

regex_pattern = r"[.,]+"

import re
print("\n".join(re.split(regex_pattern, input())))


# In[101]:


## 58) Group(), Groups() & Groupdict()

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
        


# In[102]:


## 59) Re.findall() & Re.finditer()

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))


# In[103]:


## 60) Re.start() & Re.end()

S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: 
    print ("(-1, -1)")
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)


# In[105]:


## 61) Validating Roman Numerals

thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand,hundred,ten,digit)	# Do not delete 'r'.


import re
print(str(bool(re.match(regex_pattern, input()))))


# In[109]:


## 62) Validating phone numbers

import re
[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]


# In[108]:


## 63) Validating and Parsing Email Addresses

import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)


# In[113]:


## 64) Hex Color Code

import re
pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern,input()):print(x)


# In[114]:


## 65) HTML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):        

        print ('Start :',tag)

        for ele in attrs:

            print ('->',ele[0],'>',ele[1])

            

    def handle_endtag(self, tag):

        print ('End   :',tag)

        

    def handle_startendtag(self, tag, attrs):

        print ('Empty :',tag)

        for ele in attrs:

            print ('->',ele[0],'>',ele[1])

            

MyParser = MyHTMLParser()

MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))


# In[116]:


## 66) HTML Parser - Part 2
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment  ", data, sep="\n")
        else:
            print(">>> Single-line Comment  ", data, sep="\n")
    def handle_data(self, data):

            if data != "\n":

                print(">>> Data", data, sep="\n")
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[117]:


## 67) Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser 
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[118]:


## 68) Validating UID

import re
for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


# In[119]:


## 69) Validating Credit Card Numbers

import re

for _ in range(int(input())):

    s = input()

    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):

        print("Valid")

    else:

        print("Invalid")


# In[122]:


## 70) Regex Substitution

for _ in range(int(input())):
    line = input()
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    print(line)


# In[123]:


## 71) Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[134]:


## 72) Matrix Script
import math
import os
import random
import re
import sys



n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))


# In[ ]:


## XML


# In[132]:


## 73) XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return(len(node.attrib) + sum(get_attr_number(child) for child in node))

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[136]:


## 74) XML2 - Find the Maximum Depth

import xml.etree.ElementTree as etree
global maxdepth
maxdepth = -1
def depth(elem, level):
    global maxdepth
    # your code goes here
    if level == maxdepth:
        maxdepth+=1
    for child in elem:
        depth(child, level + 1)
        

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# In[ ]:


## Closures and Decorations


# In[138]:


## 75) Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+c[-10:-5]+" "+c[-5:]for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


## 76) Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner


# In[145]:


## Numpy


# In[146]:


## 77) Arrays

import numpy

def arrays(arr):
    
    
    # complete this function
    # use numpy.array
 
    return (numpy.array(arr[::-1], float))
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[147]:


## 78) Shape and Reshape

import numpy

print(numpy.array(input().split(),int).reshape(3,3))


# In[148]:


## 79) Transpose and Flatten

import numpy

a, b = map(int, input().split())

res = numpy.array([input().strip().split() for _ in range(a)], int)
print(res.transpose())
print(res.flatten())


# In[150]:


## 80) Concatenate

import numpy

a, b, c = map(int, input().split())

res_a = numpy.array([input().split() for _ in range(a)], int)
res_b = numpy.array([input().split() for _ in range(b)], int)

print(numpy.concatenate((res_a,res_b), axis = 0))


# In[151]:


## 81) Zeros and Ones

import numpy

n = tuple(map(int, input().split()))

res_a= numpy.zeros(n, dtype=numpy.int)
res_b= numpy.ones(n, dtype=numpy.int)

print(res_a)
print(res_b)


# In[152]:


## 82) Eye and Identity

import numpy

res = str(numpy.eye(*map(int, input().split()))).replace('1',' 1').replace('0', ' 0')

print(res)


# In[153]:


## 83) Array Mathematics

import numpy

n, m = map(int, input().split())
a, b = (numpy.array([input().split() for _ in range (n)], dtype= int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')


# In[154]:


## 84) Floor, Ceil and Rint

import numpy

numpy.set_printoptions(sign = ' ')

a = numpy.array(input().split(),float)

res_a = numpy.floor(a)
res_b = numpy.ceil(a)
res_c = numpy.rint(a)

print(res_a)
print(res_b)
print(res_c)


# In[155]:


## 85) Sum and Prod

import numpy

n, m = map(int, input().split())

a = numpy.array([input().split() for _ in range (n)],int)

res = numpy.prod(numpy.sum(a, axis=0), axis=0)

print(res)


# In[156]:


## 86) Min and Max

import numpy

res = numpy.max(numpy.min(numpy.array([input().split() for _ in range(int(input().split()[0]))], int), axis= 1))

print(res)


# In[157]:


## 87) Mean, Var, and Std

import numpy 

n, m = map(int, input().strip().split())

arr = numpy.array([ input().strip().split() for _ in range(n) ], int)

m = numpy.mean(arr, axis = 1)
v = numpy.var(arr, axis = 0)
std = round(numpy.std(arr, axis = None),11)

print(m)
print(v)
print(std)


# In[158]:


## 88) Dot and Cross

import numpy

n = int(input())

a = numpy.array([input().split() for _ in range (n)], int)
b = numpy.array([input().split() for _ in range (n)], int)
res = numpy.dot(a,b)

print(res)


# In[159]:


## 89) Inner and Outer

import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)



print(numpy.inner(a, b))
print(numpy.outer(a, b))


# In[160]:


## 90) Polynomials

import numpy

c = list(map(float,input().split()))
x = input()
print(numpy.polyval(c, int(x)))


# In[161]:


## 91) Linear Algebra

import numpy

numpy.set_printoptions(legacy='1.13')



n = int(input())
a = numpy.array([input().strip().split() for _ in range(n)], float)



print(numpy.linalg.det(a))


# In[ ]:


## PROBLEM 2


# In[162]:


## 1) Birthday Cake Candles

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    c = candles
    return c.count(max(c))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[163]:


## 2) Number Line Jumps

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    x1 = x1
    v1 = v1
    x2 = x2
    v2 = v2
    if v1 > v2:
        if (x1-x2)%(v1-v2)==0:
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# In[164]:


## 3) Viral Advertising

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    p = 5
    res = 0
    for _ in range(n):
        clnt = p//2
        p = clnt*3
        res = clnt + res
        
        
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[165]:


## 4) Recursive Digit Sum

import math
import os
import random
import re
import sys

def superDigit(n, k):
    a = sumdigit(n)
    return sup_digit(str(int(a)*k))

def sumdigit(n):
    res = 0
    for i in n:
        res+=int(i)
    return str(res)

def sup_digit(n):
    if len(n) == 1:
        return n
    else:
        return sup_digit(sumdigit(n))
        
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# In[166]:


## 5) Insertion Sort - Part 1

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and val < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
            print(*arr, sep= ' ')
        arr[pos] = val
    print(*arr, sep= ' ')
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# In[167]:


## 6) Insertion Sort - Part 2

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
        n = len(arr)
        for i in range(1, n):
            val = arr[i]
            pos = i
            while pos > 0 and val < arr[pos - 1]:
                arr[pos] = arr[pos - 1]
                pos -= 1
            arr[pos] = val
            print(*arr, sep= ' ')
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

