#coding:utf-8
import os
import glob

case_path=r"C:\svn\NewAutoTest\PKG_OTCTS_V1.0.5.4"
#lbm_list=os.getcwd()+os.sep+"my_lbm_list.txt"
'''
if os.path.exists(lbm_list):
    os.remove(lbm_list)
'''
cnt = 0
lbmcase='L2600010'
#with open(lbm_list,'a',encoding='gbk') as list_file:
try:
    for file in glob.glob(case_path+os.sep+"**"+os.sep+"*.txt",recursive=True):
        case_file_name= os.path.split(file)
        case_name = case_file_name[1].split('.',1)[0]
        cnt+=1
        #print(cnt, file)
        try:
            with open(file,'r',encoding = "UTF-8") as case_file:
                for line in case_file:
                    pos = line.find(lbmcase)
                    if(pos>0):
                        print(file)  
                        break
        except Exception:
            with open(file,'r',encoding = "GBK") as case_file:
                for line in case_file:
                    pos = line.find(lbmcase)
                    if(pos>0):
                        print(file)  
                        break
except Exception as e:  
    print(Exception,":",e)
os.system("pause")