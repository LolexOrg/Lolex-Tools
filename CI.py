import os, py_compile
folders = []
files = []
root = os.listdir("./")
arraypos = 0
while arraypos < len(root):
    if (".git" in root[arraypos]) == False:
        if "." in root[arraypos] or "LICENSE" in root[arraypos]:
            length = len(root[arraypos])
            p = root[arraypos][length - 3]
            y = root[arraypos][length - 2]
            dot = root[arraypos][length - 4]
            if p == "p" and y == "y" and dot == ".":
                files.append("./" + root[arraypos])
            else:
                folders.append("./" + root[arraypos])
    arraypos = arraypos + 1
arraypos = 0
while arraypos<len(folders):
    path = folders[arraypos]
    currsub = os.listdir(path)
    tarraypos = 0
    sublen = len(currsub)
    while tarrypos<sublen:
        if (".git" in root[arraypos]) == False:
            
            if "." in root[arraypos]:
                clen = len(currsub[tarraypos])
                p = currsub[tarraypos][clen - 3]
                y = currsub[tarraypos][clen - 2]
                dot = currsub[tarraypos][clen - 4]
                if p == "p" and y == "y" and dot == ".":
                    files.append(path + currsub[tarraypos])
                else:
                    folders.append(path + currsub[tarraypos])
          tarraypos = tarraypos + 1
      arraypos = arraypos + 1
flen = len(files)
arraypos = 0
while arraypos<flen:
  currfile = file[arraypos]
  py_compile.compile(currfile)
  print("Successfully compiled " + currfile)
  arraypos = arraypos + 1
        
                
                
            
