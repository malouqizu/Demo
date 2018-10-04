import xml.etree.cElementTree as ET
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='result.log',
                    filemode='w')

#src_path:input path  tag_path:you need dir name and return absolute path of you need dir
def find_dir(src_path,tag_path):	
    for fpathe,dirs,fs in os.walk(src_path):
        for d in dirs:
            if d==tag_path:
                return fpathe+"\\"+tag_path

#get absolute path of all xml file under target dir 
def get_xml_list(xml_dir):
    lst = []
    for file_name in os.listdir(xml_dir):
        if file_name.endswith(".xml"):
            lst.append(xml_dir+"/" + file_name)
    return lst

#open one xml file
def open_xml(path):
    try:
        return ET.parse(path)
    except IOError as io:
        print ()
        logging.error(str(io))
    except FileNotFoundError as fnfe:
        print(str(fnfe))
        logging.error(fnfe)
    except Exception as e:
        print(path,":", e)
        logging.error(path+" : "+str(e))

if __name__ == "__main__":
    startdir = sys.argv[1]
    target = sys.argv[2]
    cases_path = find_dir(startdir, target)	
    if cases_path is None:
        print("not found tag_path")
        exit(1)
		
    cases_path = cases_path.replace("\\","/")
    cases_path_list = get_xml_list(cases_path)  # get all case file
    oper_path_list = get_xml_list(cases_path+"/"+"Operation")   #get all operation file
    
    oper_dict = {}      # key is Operation's name,value is startswith'$' 
    for oper in oper_path_list:
        xml_abs_path = oper
        oper_tree = open_xml(xml_abs_path)
        if oper_tree is None:
            continue
        list_oper_text = ""
        for element in oper_tree.iter():
            if isinstance(element.text, str) and element.text.startswith("$"):
                list_oper_text += element.text
        if list_oper_text != None:
            pos = xml_abs_path.rfind("/")
            oper_dict[xml_abs_path[pos+1:].replace(".xml","")] = list_oper_text

    #after finishing oper_dict, start to check case. when find Operation in case, go to match oper_dict,
    #if match successfully, just to pass
    #else log error
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
                                print(check_case_list[0]+"---"+check_case_list[1]+"---"+item+"---NO")
                                logging.error(check_case_list[0]+"---"+check_case_list[1]+"---"+item+"---NO")
                        except KeyError as e:   
                            print(str(e)+" be not found in Operation")
                            logging.error(str(e)+" be not found in Operation")
                        except Exception as e:
                            print(e)
                            logging.error(e)
    print ("finish!")
    exit(0)

