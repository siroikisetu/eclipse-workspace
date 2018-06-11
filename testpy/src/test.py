#print('true' if 1==2 else "false")
# generator version
'''
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
for x in fibon(100):
    print(x)
'''
'''
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
for x in fibon(1000):
    print(x)
'''
'''
def multiply(x):
    return (x**x)
def add(x):
    return (x+x)
funcs = [multiply, add]
for i in range(5):
    value = map(lambda x:x(i), funcs)
    print(list(value))
'''
'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
'''
