import xml.etree.cElementTree as ET
import os
import re
import copy

def get_xml_list(xml_dir):
    lst = []
    for file_name in os.listdir(xml_dir):
        if file_name.endswith(".xml"):
            lst.append(xml_dir+"/" + file_name)
    return lst

def open_xml(path):
    try:
        return ET.parse(path)
    except Exception as e:
        print(path,":", e)

#xmlFileName : list_oper_text   
dict_oper={}
#{$keyWord}...
list_oper_text=""
j=0
list_xml_oper = get_xml_list("./Operation")
for oper_path in list_xml_oper:
    xml_abs_path = oper_path
    #xml_abs_path = "./Operation/Select_A_Wanted_Audio_File.xml"
    oper_tree = open_xml(xml_abs_path)
    if oper_tree is None:
        continue
    list_oper_text=""
    for element in oper_tree.iter():       
        if  isinstance(element.text,str) and element.text.startswith("$"):         
            list_oper_text+=element.text
    if list_oper_text != None:
        dict_oper[xml_abs_path[12:-4]] =  list_oper_text
#print (dict_oper)

#--------------------------------------------------------------------------------------------------------

list_check=[]
#path|pathValue|paramValue
list_path_para=""
list_case = get_xml_list(".")

for case_path in list_case:
    #case_tree = open_xml("./TC_MEDIA_SD_0172.xml")
    #print (case_path)
    case_tree = open_xml(case_path)
    if case_tree is None:
        continue
    list_path_para=""
    for case_e in case_tree.iter():
        if case_e.tag == "operation" and "path" in case_e.attrib.keys():
            list_path_para= case_path+"|"
            list_path_para+=case_e.attrib["path"]+"|"
            for p in case_e:
                if "name" in p.attrib.keys():
                    list_path_para+=p.attrib["name"]+"_"
            list_check.append(list_path_para)
#print (list_check)
#-----------------------------------------------------------------------------------------------------------
for case_item in list_check:
    temp_list = case_item.split("|")
    para_list = temp_list[2].split("_")
    for p in para_list:
        if p == "":
            continue
        try:
            if p in dict_oper[temp_list[1]]:
               pass
            else:
               print (temp_list[0],temp_list[1],p,"is no")
               continue
        except Exception as e:
            print (temp_list[0]," ", "not found ",e," in Operation")
            continue
 




