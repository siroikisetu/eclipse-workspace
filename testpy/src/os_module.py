#coding:utf-8
import os

'''获取当前目录'''
cur_dir=os.getcwd()
print("当前目录：",cur_dir)
print("当前工作目录",os.curdir)
'''指示你正在使用的工作平台。比如对于Windows，
它是'nt'，而对于Linux/Unix用户，它是posix'''
print("工作平台:",os.name)

'创建目录'
dir=cur_dir+os.sep+'dir_test'
if not os.path.exists(dir):
    os.mkdir(dir)

'创建空文件'
file=dir+os.sep+'test.txt'
if not os.path.exists(file):
    fp=open(file,'w')
    fp.close()
'删除文件'   
if os.path.exists(file):
    os.remove(file)

'删除目录'
if os.path.exists(dir):
    os.rmdir(dir)

'删除多个目录'
if os.path.exists(dir):
    os.removedirs(dir)

'返回一个路径的目录名和文件名'
if os.path.isfile(cur_dir+os.sep+'test.py'):
    print(os.path.split(cur_dir+os.sep+'test.py'))

if os.path.isdir(cur_dir):
    print(cur_dir)
    
'''返回指定目录下的所有文件和目录名,默认当前目录'''
for file in os.listdir():
    print(file)
    '获取文件属性'
    '''print(os.stat(file)[2])'''
