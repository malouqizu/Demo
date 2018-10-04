import xml.etree.cElementTree as ET
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='result.log',
                    filemode='w')

#get all xml of directory 
def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file).replace("\\","/"))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file).replace("\\","/"))
            else:
                files_list.append(os.path.join(root, special_file).replace("\\","/"))
    return files_list

#open a xml file
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

#pack a dict, key:operation's name without postfix; value: str of startswith "$"	
def pack_oper_dict(pod_list):
    pod_oper_dict = {}  # key is Operation's name,value is startswith'$'
    for oper in pod_list:
        oper_tree = open_xml(oper)
        if oper_tree is None:
            continue
        list_oper_text = ""
        for element in oper_tree.iter():
            if isinstance(element.text, str) and element.text.startswith("$"):
                list_oper_text += element.text
        if list_oper_text != None:
            pos = oper.rfind("/")
            pod_oper_dict[oper[pos + 1:].replace(".xml", "")] = list_oper_text
    return pod_oper_dict

#open case and read , when meeting Operation,just to match oper_dict
def check_case_oper(cco_list):
    for case in cco_list:
        case_tree = open_xml(case)
        if case_tree is None:
            continue
        for case_e in case_tree.iter():
            if case_e.tag == "operation" and "path" in case_e.attrib.keys():
                check_case_list = []
                pos = case.rfind("/")
                check_case_list.append(case[pos + 1:])  #first item:add caseName
                check_case_list.append(case_e.attrib["path"])   #second item:add path
                for p in case_e:
                    if "name" in p.attrib.keys():
                        check_case_list.append(p.attrib["name"])    #third item: add param

                #when one operation(check_case_list) was packaged,we just to match oper_dict
                # i : Because first item of check_case_list is xml file name, second item of check_case_list is operation path name
                #  from thrid item,they are param of operation,we need to check param
                i=0
                for item in check_case_list:
                    if i<2:
                        i+=1
                        continue
                    else:
                        try:
                            # check_case_list[1] is case's operation-->path-->value
                            # item has '$' param
                            if item in oper_dict[check_case_list[1]]:
                                pass
                            else:
                                print(check_case_list[0]+"---"+check_case_list[1]+"---"+item+"---NO")
                                logging.error(check_case_list[0]+"---"+check_case_list[1]+"---"+item+"---NO")
                        except KeyError as e:   
                            print(check_case_list[0]+str(e)+" be not found in Operation")
                            logging.error(check_case_list[0]+str(e)+" be not found in Operation")
                        except Exception as e:
                            print(e)
                            logging.error(e)
	

if __name__ == "__main__":
    try:
        cases_path = sys.argv[1]
        oper_path = sys.argv[2]
    except Exception  as e:
        print ("The path of cases or operation is illegal!")
        logging.error("The path of cases or operation is illegal!")
    finally:
        exit(1)
    		
    cases_path = cases_path.replace("\\","/")
    oper_path = oper_path.replace("\\","/")

    cases_path_list = scan_files(cases_path,None,".xml")  # get all case file
    oper_path_list = scan_files(oper_path,None,".xml")   #get all operation file

    oper_dict = pack_oper_dict(oper_path_list)
    check_case_oper(cases_path_list)
   
    print ("finish!")
    logging.info("finish!")
    exit(0)
