#coding:utf-8
import os
import glob

def findlbmmodule(file,coding):
    with open(file,'r',encoding=coding) as lbm_file:
        for line in lbm_file:
            pos = line.find('模块名称')
            if(len(line[pos:-1]) <= 5):
                pos = line.find('模块描述')
            if(pos>0):
                module = line[pos:-1]
                break            
    lbm_file.close()
    return(module)
    
lbm_path_old=r"C:\svn\Test\OTCTS_V1.0.5.4_基础类重构\src\otcts_old\lbm"
lbm_path_new=r"c:\svn\Test\OTCTS_V1.0.5.4_基础类重构\src\otcts"
lbm_list=os.getcwd()+os.sep+"check_lbm_list.txt"

if os.path.exists(lbm_list):
    os.remove(lbm_list)
cnt = 0
try:
    with open(lbm_list,'a',encoding='gbk') as list_file:
        for file in glob.glob(lbm_path_old+os.sep+"L[0-9]*.cpp"):
            lbm_file_name = os.path.split(file)
            exist_lbm = glob.glob(lbm_path_new+os.sep+"*"+os.sep+"*lbm*"+os.sep+lbm_file_name[1])
            module = ""
            if not exist_lbm:
                lbm_name = lbm_file_name[1].split('.',1)[0]
                try:
                    module = findlbmmodule(file, "GBK")
                except Exception:
                    module = findlbmmodule(file, "utf-8")
                cnt+=1 
                print(lbm_name+module)
                list_file.writelines(lbm_name+module+'\n')                   
        print(cnt)
        print('cnt = {0}'.format(cnt))
        list_file.writelines("cnt = {0}".format(cnt))
        list_file.close()
except Exception as e:  
    print(Exception,":",e) 
os.system("pause")



