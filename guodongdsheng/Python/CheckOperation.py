import xml.etree.cElementTree as ET
import os
import re

oper = "operation"
oper_path = "path"
oper_path_value = ""
oper_param_name_value = ""
GM_param_value=""

is_found_oper = False
res = False

i=0
def open_xml(path):
    try:
        return ET.parse(path)
    except Exception as e:
        print( path,"has Error:", e)


#获取.xml文件路径放到list中
xml_file_path_list=[]
for file_name in os.listdir("./"):
    if file_name.endswith(".xml"):
        xml_file_path_list.append("./"+file_name)


#对每一个路径（文件）进行操作
for file_path in xml_file_path_list:
    is_found_oper = False
    res = False
    xml_abs_path = "./[GM][MY17][HMI][Audio][][Android5.1]TC_Personalization_0180.xml"
    #xml_abs_path = file_path
    case_tree = open_xml(xml_abs_path)
    if case_tree is None:
        continue
    for element in case_tree.iter():
        if element.tag == oper: #找到operation节点
            is_found_oper = True
            if oper_path in element.attrib.keys(): #如果有operation的path属性
                oper_path_value = element.attrib["path"]#取出path值：调用的文件名
                for p in element.iter():
                    if "name" in p.attrib.keys():
                        oper_param_name_value = p.attrib["name"] #取出param name 的值：参数

    if is_found_oper is False: #xml文件里就没有operation标签
        res = True

    if oper_path_value!="" and res == False:
        oper_tree = open_xml("./Operation/"+oper_path_value+".xml")
        if oper_tree is None:
            continue
        for element in oper_tree.iter():
            if  element.tag =="param" and "name" in  element.keys():
                #print("111111111111",element.text)
                print(element.text[2:-1],"  ",oper_param_name_value)
                if  element.text[2:-1] == oper_param_name_value:
                    res = True
                    break
    if res==False:
        print(xml_abs_path,"---> result --->",res)
        i+=1
print(i)
