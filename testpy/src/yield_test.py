#coding=utf-8
import sys
'迭代器'
list=['a','v','l','k']
it=iter(list)
for i in it:
    print(i,end=" ")
    
'''
生成器
'''
def fun(n):
    for i in range(n):
        yield i
    return
f=fun(5)
for i in f:
    print(i,end=' ')
'''
while f :
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
'''

        