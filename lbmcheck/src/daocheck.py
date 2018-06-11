#coding:utf-8
import os
import glob
    
lbm_path_old=r"C:\svn\Test\OTCTS_V1.0.5.4_基础类重构\src\otcts_old\dao_esql"
lbm_path_new=r"c:\svn\Test\OTCTS_V1.0.5.4_基础类重构\src\otcts"
lbm_list=os.getcwd()+os.sep+"dao_list.txt"

if os.path.exists(lbm_list):
    os.remove(lbm_list)
cnt = 0
try:
    with open(lbm_list,'a') as list_file:
        for file in glob.glob(lbm_path_old+os.sep+"*.sqx"):
            lbm_file_name = os.path.split(file)
            exist_lbm = glob.glob(lbm_path_new+os.sep+"*"+os.sep+"dao_esql"+os.sep+lbm_file_name[1])
            module = ""
            if not exist_lbm:
                print(lbm_file_name[1])
                list_file.writelines(lbm_file_name[1]+'\n') 
                cnt+=1                  
        print(cnt)
        print('cnt = {0}'.format(cnt))
        list_file.writelines("cnt = {0}".format(cnt))
        list_file.close()
except Exception as e:  
    print(Exception,":",e) 
os.system("pause")



