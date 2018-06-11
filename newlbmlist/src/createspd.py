#coding:UTF-8
import os
import glob
def GetModulename(file,encoding):
    with open(file,'r',encoding=encoding) as lbm_file:
        module=' '
        for line in lbm_file:
            pos = line.find("extern")
            if(pos>=0):
                start_pos=line.find("*")+1
                end_pos=line.find("(")
                module=(line[start_pos:end_pos]).strip()
                break
    return module
src_path = input("please input lbm path:")
if os.path.exists("KCBPSPD.xml"):
    os.remove("KCBPSPD.xml")
lbm_cnt = 0 
try:
    with open("KCBPSPD.xml",'a',encoding='gbk') as spd_file:
        spd_file.writelines('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n<kcbpspd>\n')
        for file in glob.glob(src_path+os.sep+"L[0-9]*.cpp"):
            lbm_name= (os.path.split(file))[1].split('.',1)[0]
            module=' '
            print(lbm_name)
            try:
                module=GetModulename(file, 'gbk')
            except UnicodeDecodeError:
                try:
                    module=GetModulename(file, 'utf-8')
                except UnicodeDecodeError:
                    module=GetModulename(file, 'utf-16')
            str = '''<program acm="public" cache="no" comment="" concurrence="-1" name="'''+lbm_name+'''" path="KBSS_BASE.DLL" module="'''+module+'''" node="0"  priority="1" rsl="1" timeout="60" type="biz" userexitnumber="10" xa="0"/>\n'''
            spd_file.writelines(str)
            lbm_cnt+=1
        spd_file.writelines('</kcbpspd>')
        print("cnt={}".format(lbm_cnt))
except Exception as e:  
    print(Exception,":",e)
os.system("pause")
    
        
        



