#coding=utf-8
import re
'''
key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print(matcher1.group(0))#打印出来
'''
'''
key = r"chuxiuhong@hit.edu.cn"
p1 = r"@.+\."#我想匹配到@后面一直到“.”之间的，在这里是hit
pattern1 = re.compile(p1)
'''
'''
key = r"saas and sas and saaas"
p1 = r"sa{2}s"
pattern1 = re.compile(p1)
'''
key = r"192.168.201.138"
#p1 = r"(\d{1,3}\.){3}\d{1,3}"
p1 = r"\d{1,3}" 
pattern1 = re.compile(p1)
'''
matcher1 = re.search(pattern1,key)
print(matcher1.group())
'''
print(pattern1.findall(key))