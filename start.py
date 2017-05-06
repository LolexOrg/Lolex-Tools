#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, platform, shutil, sys, time
sys.path.extend(("./lib/"))
a = time.time()
print("Detecting system...")
system = platform.system()
if "arm" in platform.platform():
	try:
		import androidinit
		try:
			os.remove("./ver_old.py")
		except(IOError, OSError):
			pass
		os.rename("./ver.py","ver_old.py")
		shutil.copy("/sdcard/Lolex-Tools/ver.py","./")
		import ver, ver_old
		if ver.version>ver_old.version:
			print("Installing updates...")
			os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
	except(ImportError):
		os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
try:
        fail = False
        try:
                import JTToolsOptions
                try:
                        os.rename("./JTToolsOptions.py","LolexToolsOptions.py")
                except(IOError, OSError):
                        try:
                                os.rename("./JTToolsOptions.pyc","LolexToolsOptions.pyc")
                        except(IOError, OSError):
                                pass
        except(ImportError, SystemError):
                fail = True
        if fail != False:
                import LolexToolsOptions
                if LolexToolsOptions.compiledon<8.127:
                        if platform.system() == "Windows":
                                if sys.version_info.minor>5:
                                        os.system(" py .\setup\generic\LolexToolsInstaller.py")
                                else:
                                        os.system("python .\setup\generic\LolexToolsInstaller.py")
                        else:
                                if "arm" in platform.system():
                                        os.system("cd ./Lolex-Tools")
                                if platform.system() == "Linux":
                                        os.system("python3 ./setup/generic/LolexToolsInstaller.py")
                try:
                        import ver
                        if ver.version <= 8.129211346:
                                with open ("./exitsettings.py","a") as f: f.write("hidden = False")
                except(IOError, ImportError):
                        pass
except(ImportError, IOError, OSError):
        if platform.system() == "Windows":
                if sys.version_info.minor>5:
                        os.system("py .\setup\generic\LolexToolsInstaller.py")
                else:
                        os.system("python .\setup\generic\LolexToolsInstaller.py")
        else:
                os.system("python3 ./setup/generic/LolexToolsInstaller.py")
if system == "Windows":
        print("Starting on Windows...")
        os.system("TITLE Lolex-Tools")
        os.system("MODE 1000")
        if sys.version_info.minor>5:
                os.system("py .\sys/bootanim.py")
                print("Starting...")
                b = time.time()
                local = time.asctime(time.localtime(time.time()))
                with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
                        outf.write(local)
                        outf.write("	 Took ")
                        outf.write((str(b-a)))
                        outf.write("seconds to initilaize on Windows Python >3.5\n")
                time.sleep(3)
                os.system("py .\LolexTools.py")
        else:
                os.system("python .\sys/bootanim.py")
                print("Starting...")
                b = time.time()
                local = time.asctime(time.localtime(time.time()))
                with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
                        outf.write(local)
                        outf.write("	 Took ")
                        outf.write((str(b-a)))
                        outf.write("seconds to initilaize on Windows Python < 3.6.\n")
                time.sleep(3)
                os.system("python LolexTools.py")
        exit(None)
else:
        print("Starting on Linux...")
        sys.stdout.write("\x1b]2;Lolex-Tools\x07")
        os.system("sudo apt-get install xdotool")
        os.system("xdotool key ctrl+super+Up")
        os.system("python3 ./sys/bootanim.py")
        print("Starting...")
        b = time.time()
        local = time.asctime(time.localtime(time.time()))
        with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
                outf.write(local)
                outf.write("	 Took ")
                outf.write((str(b-a)))
                outf.write("seconds to initilaize on Linux Python 3.\n")
        time.sleep(3)
        os.system("python3 ./LolexTools.py")
        exit(None)
