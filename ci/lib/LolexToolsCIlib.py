#! python3
# 0
#  0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
#   0              00     0  0         0           00             00       0      0    0      0   0          0
#    0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
#     0            00     0  0         0          0  0            00       0      0    0      0   0              0
#      0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
# 
# authors = Monkeyboy2805
import sys
import os
import py_compile

sys.path.insert(0, "./ci/build/prop")
import LATEST_PYTHON_VERSION as PY_VER

del sys.path[sys.path.index("./ci/build/prop")]


def get_py_ver():
	return (str(sys.version_info[0])) + (str(sys.version_info[1])) + (str(sys.version_info[2])) + (
		str(sys.version_info[4]))


def update_py_ver():
	if PY_VER.version < int(get_py_ver()) and sys.version_info[3] == "final":
		os.remove("./ci/build/prop/LATEST_PYTHON_VERSION.py")
		with open("./ci/build/prop/LATEST_PYTHON_VERSION.py", "a") as outf:
			outf.write("version = " + str(get_py_ver()))
			print("Found version was bigger than expected")
		os.system("git add *")
		os.system("git commit -am '[ci skip] Update python version in ci/build to " + str(get_py_ver()) + "'")
		if os.system("git pull --rebase") != 0:
			exit(127)
		os.system("git push")


def update_headers():
	# Need to add project header (well, the ability for it to do so)
	if int(get_py_ver()) == int(PY_VER.version):
		print("Updating headers...")
		files = get_file_folders()
		for j in range(0, len(files) - 1):
			file_opened = open(files[j], "r+")
			file_opened_lines = file_opened.readlines()
			if file_opened_lines[0] != "#! python3\n":
				file_opened_lines.insert(0, "#! python3\n")
				file_opened.close()
				os.remove(files[j])
				with open(files[j], "a") as outf:
					for i in range(0, len(file_opened_lines)):
						if i == len(file_opened_lines):
							break
						outf.write(file_opened_lines[i])
				os.system("git add *")
				os.system("git commit -am '[ci skip] Update shebang line in " + files[j] + "'")
				# os.system("git branch $TRAVIS_BUILD_NUMBER AUTOMATION")
				if os.system("git pull --rebase") != 0:
					os.system("127")
				os.system("git push")
				file_opened.close()


def get_file_folders():
	folders = []
	files = []
	root = os.listdir("./")
	arraypos = 0
	while arraypos < len(root):
		if not (".git" in root[arraypos]):
			readin = True
			try:
				r = open(root[arraypos], "r")
				r.close()
			except(IOError, OSError):
				readin = False
			if readin:
				if root[arraypos].endswith(".py"):
					files.append("./" + root[arraypos])
			if not readin:
				readin2 = True
				try:
					os.listdir(root[arraypos])
				except(IOError, OSError):
					readin2 = False
				if readin2:
					folders.append("./" + root[arraypos])
		arraypos = arraypos + 1
	arraypos = 0
	while arraypos < len(folders):
		path = folders[arraypos] + "/"
		currsub = os.listdir(path)
		tarraypos = 0
		sublen = len(currsub)
		while tarraypos < sublen:
			if not (".git" in currsub[tarraypos]):
				readin3 = True
				try:
					r = open(path + currsub[tarraypos])
					r.close()
				except(IOError, OSError):
					readin3 = False
				if readin3:
					if currsub[tarraypos].endswith(".py"):
						files.append(path + currsub[tarraypos])
				if not readin3:
					readin4 = True
					try:
						os.listdir(path + currsub[tarraypos])
					except(IOError, OSError):
						readin4 = False
					if readin4:
						folders.append(path + currsub[tarraypos])
			tarraypos = tarraypos + 1
		arraypos = arraypos + 1
	return files


def compile_files(files):
	failers = 0
	flen = len(files)
	arraypos = 0
	print("Compiling...")
	fail = False
	while arraypos < flen:
		currfile = files[arraypos]
		if type(py_compile.compile(currfile)) is str:
			print("Successfully compiled " + (str(currfile)))
		else:
			print("Failed to compile " + (str(currfile)))
			fail = True
			failers = failers + 1
		arraypos = arraypos + 1
	if fail:
		print(str(failers) + " files failed to compile")
		exit(1)


def inactivity_reset():
	os.remove("./ci/build/stats.py")
	with open("./ci/build/stats.py", "a") as outf:
		outf.write("inactivity = 0")
