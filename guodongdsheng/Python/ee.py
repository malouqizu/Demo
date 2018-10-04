import os
import sys

def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))
    return files_list



if __name__ == "__main__":
    l1 = scan_files("F:\\Project\\NewCase\\MATS\\info3\\my17\\scripts", None, ".xml")
    for item in l1:
        print(item)
    print(len(l1))
