import sys
import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./result.log',
                    filemode='w')

def copy_cases(cc_directory_list):
    for item_list in cc_directory_list:
        i = 0
        for item in item_list:
            if i < 2:
                i += 1
                continue
            else:
                try:
                    if item.startswith("/"):
                        src_path = item_list[0] + item
                    else:
                        src_path = item_list[0] + "/" + item
                    dst_path = "../script_release/" + src_path.replace("../bj/", "").replace("/", ".")
                    shutil.copytree(src_path, dst_path)
                    if item_list[1] is not "":
                        f = open(dst_path + "/" + item_list[1].strip()+ ".txt", "w")
                        f.close()
                    i += 1
                except IOError as io:
                    i+=1
                    logging.error(io)
                    print(str(io))
                except Exception as e:
                    i += 1
                    logging.error(e)
                    print(str(e))


def read_Precondition_Group_Definition_txt(rpgd_path):
    rpgd_directory_list = []
    with open(rpgd_path, "r") as f:
        line_list = []
        parent_dir = ""
        author = ""
        for line in f.readlines():
            line = line.strip()
            if line.startswith(".."):
                parent_dir = line.split(":")[0]
                author = line.split(":")[1]
                rpgd_directory_list.append(line_list)
                line_list = []
                flag = True
                line_list.append(parent_dir)  # parent dir
                line_list.append(author)  # author
            elif line.startswith("/"):
                if flag is True:
                    line_list[0]=line_list[0]+line
                    flag = False
                else:
                    rpgd_directory_list.append(line_list)
                    line_list = []
                    line_list.append(parent_dir+line)  # parent dir
                    line_list.append(author)  # author
            elif line == "":
                continue
            else:
                line_list.append(line)
    del rpgd_directory_list[0]
    return rpgd_directory_list


if __name__ == "__main__":

    if len(sys.argv)<2:
        print("too few arguments")
        exit(1)

    input_path = sys.argv[1]
    txt_name =  sys.argv[2]
    input_path = input_path.replace("\\", "/")
    os.chdir(input_path)
    directory_list = read_Precondition_Group_Definition_txt(input_path + "/" + txt_name)

    if os.path.exists("../script_release"):
        shutil.rmtree("../script_release")
    os.makedirs('../script_release')
    copy_cases(directory_list)
    exit(0)
