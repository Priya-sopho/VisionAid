import os
from datetime import datetime
import speak
from shutil import copyfile,copytree,copy2

def get_drives():
    response = os.popen("wmic logicaldisk get caption")
    list1 = []
    total_file = []
    t1 = datetime.now()
    for line in response.readlines():
        line = line.strip("\n")
        line = line.strip("\r")
        line = line.strip(" ")
        if (line == "Caption" or line == ""):
            continue
        list1.append(line)
    return list1

def is_valid_path(path):
    return os.path.exists(path)

def get_directory_list(directory):
    for x in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,x)):
            if(x.endswith('.pdf')):
                print("pdf-",x)
                speak.say("pdf"+x)
            elif(x.endswith('.doc')):
                print("doc-",x)
                speak.say("doc"+ x)
            elif(x.endswith('.mp3')):
                print("audio",x)
                speak.say("audio"+ x)
            else:
                print('f-',x)
                speak.say("file"+ x)

        elif os.path.isdir(os.path.join(directory,x)):
            print ('d-', x)
            speak.say("folder"+ x)

        elif os.path.islink(os.path.join(directory,x)):
            print ('l-', x)
            speak.say("link"+ x)

        else:
            print ('---', x)
            speak.say(x)

def open_MyPc():
    list = get_drives()
    for l in list:
        print(l)
        speak.say(l)
    drive = input()
    if is_valid_path(drive):
        return drive
    else:
        speak.say("Enter correct drive")
        return 0;
    

def get_size(path):
    return os.path.getsize(path)

def open_directory(path, directory):
    path = os.path.join(path, directory)
    return path

def open_file(path, file):
    print(1)

def create_directory(path,name):
    list2 = []
    for x in os.listdir(path):
        if(x == name):
            speak.say("Folder name already exist. Please choose another name")
            return 0
    os.makedirs(os.path.join(path,name))
    return 1

def copy_file(src,dst):
    copyfile(src,dst)

def copy_directory(src,dst,symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            copy2(s, d)


def open_file(path):
    file = open(path)
    return file

def go_back(path):
    return os.path.dirname(path)

print(open_MyPc())
get_directory_list("F:\harshita")
print(create_directory("F:","ok"))
copy_file("F:\\abc.doc","G:")
copy_directory("F:\harshita","G:")
print(go_back("F:\harshita\hg"))