#coding:utf-8
import os
import glob

lbm_path_new=r"c:\svn\Test\OTCTS_V1.0.5.4_基础类重构\src\otcts"
lbm_list=os.getcwd()+os.sep+"my_lbm_list.txt"

if os.path.exists(lbm_list):
    os.remove(lbm_list)
cnt = 0

with open(lbm_list,'a',encoding='gbk') as list_file:
    for file in glob.glob(lbm_path_new+os.sep+"*"+os.sep+"*"+os.sep+"L[0-9]*.cpp"):
        lbm_file_name= os.path.split(file)
        lbm_name = lbm_file_name[1].split('.',1)[0]
        module = " "
        with open(file,'r',encoding='GBK') as lbm_file:
            for line in lbm_file:
                pos = line.find('吕旺')
                if(pos>0):
                    print(lbm_name)
                    list_file.writelines(lbm_name+'\n')
                    cnt+=1
                    break
        lbm_file.close()        
    print('cnt = {0}'.format(cnt))
    list_file.writelines("cnt = {0}".format(cnt))
    list_file.close()
 
os.system("pause")