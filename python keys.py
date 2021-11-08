st="subhani shaik welcome"
s1=st.capitalize()
print(s1)
s2=st.upper()
print(s2)
print(s2.isupper())
a="subhani shaik"
b=a.replace('shaik', 'Python')
print(b)
c=a.join('ullu')
print(c)
a='123'
b=a.isdigit()
print(b)
d='123abc'
D='abc'
c=d.isalnum()
print(c)
e=D.isalpha()
print(e)
import collections
de=collections.deque([1,2,3])
print(de)
de.appendleft(6)
print(de)


a=[1,2,3,4,5,6,7,8]
a.pop()
print(a)
de.popleft()
print('test:',a)
a=collections.deque([10,20,30,40])
a.appendleft(100)
print(a)
a.append(200)
print(a)

A='geeksforgeeks'
print(A)
B=[1,1,1,12,2,2,2,2,3,4,5,6,7]
C=B.count(1)
print(C)
print(len(B))
B.remove(7)
print(B)

a=[1,2,3,4,5]
a[-1]=6
print(a)


a=[]
a.append([10,20,30])
print(a)

a='subhanishaik'
a.split(',')
print(a)

a=(1,1,1,1,2,3,4,5)
b=set(a)
print(b)
A={'a':1, 'b':2, 'c':3}
B=A.keys()
print(B)
D=A.get(a)
print(D)
import functools
seq=['a', 'b', 'c', 'd']
for i in seq:
    pass
    print(i)
a=[10,20,30,40]
b=a
c=a+b
print(list(map(lambda x:x+2, a)))
print(list(filter(lambda x:x%3, a)))
print(functools.reduce(lambda x,y:x+y, c))

lis=[[567,345,234],[252,465,756,2345],[333,777,111,555]]
print(list(map(lambda x:sorted(x), lis)))




total=[]
for i in range(5):
    total.append(i)
    print('ewee:',total[i]+1)

a=[3,6,9,12,15]
a.append(a[-1]+3)
print(a)

a={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
for i,j in a.items():
    for i in a.items():
        print(i)
dictA={'a':[1,2,3], 'b':[9,-4,2], 'c':[3,9,9]}
result={}
for i,j in dictA.items():
    result[i]=sum(j)
    print(result[i])
    
    