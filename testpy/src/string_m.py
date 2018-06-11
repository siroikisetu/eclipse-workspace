#coding=utf-8
import string

'转换成数字'
'''
py3已删掉
print(string.atof('1.01'))
print(string.atoi('234'))
'''
print(int('11',2))#第二个参数指的是二进制
print(int('11',8))
print(float('1.343'))

'查找'
#print(string.find("helld world",'wo',2,8))
str='hello world'
strx='HELLO WORLD'
print(str.find("wo",7,8))
print(str.index("wo"))#找不到会报错

'转换大小写'
'第一个字母大写，其余小写'
str1=str.capitalize()
print(str1)

'全部转换为小写，对unicode适用'
str2=strx.casefold()
print("unicode大小写转化")
print(strx,str2)
'转换成大写，对unicode适用'
print(str,str.swapcase())

print("ascii大小写转换")
'转换成小写，只对ASCII适用'
print(strx,strx.lower())
print(str,str.upper())

'填充'
print(str.center(15,'#'))

'字符串中子串出现的字数'
print('ststtsts'.count('st',0,7))

'转化编码'
print(str.encode(encoding='gbk', errors='gbk fail'))

'指定结尾'
print(str.endswith('d'))

'检查字符串是否由字母和数字组成'
print('123'.isalnum(),'fdg'.isalnum(),'234sd3'.isalnum(),'%bs#123'.isalnum())

'连接'
print(''.join(('a','b','c'))) #括号括起来使其成为一个元组
print('-'.join((str,strx)))
print('-'.join(str))

'字符串长度'
print(len(str))

'去掉左边的指定字符  默认空格'
print(str.center(15,'#'),(str.center(15,'#')).lstrip('#'))

'创建字符映射的转换表'
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab);
str = "this is string example....wow!!!";
print (str.translate(trantab))

'字符串分割'
print(str.split(sep=' '))


