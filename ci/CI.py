#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, py_compile, sys
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[2] == 0 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
	IOError = OSError
print("CI version 2.0")
folders = []
files = []
root = os.listdir("./")
arraypos = 0
while arraypos < len(root):
	if (".git" in root[arraypos]) == False:
		readin = True
		try:
			r = open(root[arraypos], "r")
		except(IOError, OSError):
			readin = False
		if readin == True:
			if root[arraypos].endswith(".py"):
				files.append("./" + root[arraypos])
		else: pass
		if readin == False:
			readin2 = True
			try:
				os.listdir(root[arraypos])
			except(IOError, OSError):
				readin2 = False
			if readin2 == True:
				folders.append("./" + root[arraypos])
	arraypos = arraypos + 1
arraypos = 0
while arraypos<len(folders):
	path = folders[arraypos] + "/"
	currsub = os.listdir(path)
	tarraypos = 0
	sublen = len(currsub)
	while tarraypos<sublen:
		if (".git" in currsub[tarraypos]) == False:
			readin3 = True
			try:
				r = open(path + currsub[tarraypos])
			except(IOError, OSError):
				readin3 = False
			if readin3 == True:
				if currsub[tarraypos].endswith(".py"):
					files.append(path + currsub[tarraypos])
			else: pass
			if readin3 == False:
				readin4 = True
				try:
					os.listdir(path + currsub[tarraypos])
				except(IOError, OSError):
					readin4 = False
				if readin4 == True:
					folders.append(path + currsub[tarraypos])
		tarraypos = tarraypos + 1
	arraypos = arraypos + 1
flen = len(files)
arraypos = 0
print("Compiling...")
fail = False
failers = 0
while arraypos < flen:
	currfile = files[arraypos]
	if type(py_compile.compile(currfile)) is str:
		print("Successfully to compiled " + (str(currfile)))
	else:
		print("Failed to compile " + (str(currfile)))
		fail = True
		failers = failers + 1
	arraypos = arraypos + 1
if fail == True:
	print((str(failers)) + " files failed to compile.")
	exit(1)
if not os.path.exists("./ci/test.py") or os.path.isfile("./ci/test.py") == False:
        with open("./ci/test.py", "a") as outf: pass
        os.system("git add *")
        os.system("git commit -am 'Add missing file'")
        os.system("git push")
