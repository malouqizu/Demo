import xml.etree.cElementTree as ET
import os

class case_info:
     file_name=""
     oper_path = ""
     oper_para = []
     def __init__(self, p_file_name, p_oper_path, p_oper_para):
         self.file_name = p_file_name
         self.oper_path = p_oper_path
         self.oper_para = p_oper_name

def find_dir(src_path,tag_path):
    for fpathe,dirs,fs in os.walk(src_path):
        for d in dirs:
            if d==tag_path:
                return fpathe+"\\"+tag_path

def get_xml_list(xml_dir):
    lst = []
    for file_name in os.listdir(xml_dir):
        if file_name.endswith(".xml"):
            lst.append(xml_dir+"/" + file_name)
    return lst

def open_xml(path):
    try:
        return ET.parse(path)
    except IOError as io:
        print (io)
    except FileNotFoundError as fnfe:
        print(fnfe)
    except Exception as e:
        print(path,":", e)

if __name__ == "__main__":
    startdir = input('Please input startdir: ')
    target = input('Please input target: ')
    cases_path = find_dir(startdir, target)
    cases_path = cases_path.replace("\\","/")

    cases_path_list = get_xml_list(cases_path)  # get all case file
    oper_path_list = get_xml_list(cases_path+"/"+"Operation")   #get all operation file
    oper_dict = {}
    for oper in oper_path_list:
        xml_abs_path = oper
        # xml_abs_path = "./Operation/Select_A_Wanted_Audio_File.xml"
        oper_tree = open_xml(xml_abs_path)
        if oper_tree is None:
            continue
        list_oper_text = ""
        for element in oper_tree.iter():
            if isinstance(element.text, str) and element.text.startswith("$"):
                list_oper_text += element.text
        if list_oper_text != None:
            pos = xml_abs_path.rfind("/")
            oper_dict[xml_abs_path[pos+1:].split(".")[0]] = list_oper_text
    #i=0
    for case in cases_path_list:
        case_tree = open_xml(case)
        if case_tree is None:
            continue

        for case_e in case_tree.iter():
            if case_e.tag == "operation" and "path" in case_e.attrib.keys():
                check_case_list = []
                pos = case.rfind("/")
                check_case_list.append(case[pos + 1:])  # first item:add caseName
                check_case_list.append(case_e.attrib["path"])   #second item:add path
                for p in case_e:
                    if "name" in p.attrib.keys():
                        check_case_list.append(p.attrib["name"])    #third item: add param
                i=0
                for item in check_case_list:
                    if i<2:
                        i+=1
                        continue
                    else:
                        try:
                            if item in oper_dict[check_case_list[1]]:
                                pass
                            else:
                                print(check_case_list[0]+"---"+check_case_list[1]+"---"+"NO")
                        except KeyError as e:
                            print(e)
                        except Exception as e:
                            print(e)
