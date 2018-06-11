#coding:utf-8
import os
import glob
import chardet

case_path=r"C:\svn\NewAutoTest\PKG_OTCTS_V1.0.5.4"
#lbm_list=os.getcwd()+os.sep+"my_lbm_list.txt"
'''
if os.path.exists(lbm_list):
    os.remove(lbm_list)
'''
cnt = 0
lbmcase='L2600010'
#with open(lbm_list,'a',encoding='gbk') as list_file:
for file in glob.glob(case_path+os.sep+"**"+os.sep+"*.txt",recursive=True):
    case_file_name= os.path.split(file)
    case_name = case_file_name[1].split('.',1)[0]
    cnt+=1
    print(cnt)
    #print(cnt, file)
    with open(file,'rb') as case_file:
        content = case_file.read()
        adchar=chardet.detect(content)
        coding = "GBK"
        if adchar['encoding']:
            coding = adchar['encoding']
        case_file = content.decode(coding, errors='ignore')
        pos = case_file.find(lbmcase)
        if(pos>0):
            print(file)  
 
os.system("pause")